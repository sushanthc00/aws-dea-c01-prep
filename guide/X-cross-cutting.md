# Cross-cutting: cost, HA/DR, Regions, quotas, Well-Architected
Tags: ✓ verified 2026-10-20 (see numbered sources in `docs/sources.md`) · ~ established, not re-fetched.

## 1. Cost optimisation playbook (appears in nearly every "MOST cost-effective" stem)
| Layer | Levers |
|---|---|
| Storage | S3 classes by access pattern ✓ (Intelligent-Tiering for unknown; Glacier IR quarterly; Deep Archive); lifecycle (<128 KB don't transition ✓, min durations ✓); Parquet + compression; delete incomplete multipart / noncurrent versions; S3 Tables auto-compaction ✓ |
| Compute | right engine (Lambda <15 min ✓, Glue, EMR Serverless, Athena); Glue **Flex** ✓, auto scaling; EMR Spot for task nodes; Graviton ~; Savings Plans/RIs; Redshift Serverless vs provisioned + reservations (3-yr up to 45 % ✓); pause/resume ~ |
| Query | partitioning, pruning, columnar, `LIMIT`, workgroup scan limits ~, result reuse, MVs, SPICE for dashboards |
| Streaming | Firehose over custom consumers; batch records (Firehose bills per record rounded to 5 KB ✓); on-demand vs provisioned shards by predictability; EFO only when needed (extra cost) |
| Data transfer | same-Region processing, gateway endpoints (free ✓) vs NAT, CloudFront/Transfer Acceleration when justified, avoid cross-Region replication unless required |
| Governance | tags + Cost Explorer + Budgets (in scope ✓), cost allocation per workgroup/project, deletion/TTL of stale data |
Heuristics: *unpredictable → serverless/on-demand; steady → provisioned + commitment; cold → cheaper tier; repeated query → precompute (MV/CTAS/SPICE); non-urgent → Flex/Spot/Bulk.*

## 2. High availability, DR, backups
| Concept | Detail |
|---|---|
| Regions vs AZs | AZ failure → multi-AZ services (S3 ≥3 AZ ✓, DynamoDB, Kinesis, SQS, Aurora storage, Redshift RA3 Multi-AZ ~); One Zone classes are single-AZ ✓ |
| RPO/RTO tiers | backup & restore (hours) → pilot light → warm standby → active-active |
| Cross-Region options | S3 CRR (versioning), DynamoDB global tables, Aurora Global DB, Redshift cross-Region snapshots (+ KMS grant), AWS Backup cross-Region/account copy, MSK Replicator ✓, Kinesis (producer dual-write/Firehose), Route 53 failover ~ |
| Resilient pipelines | decoupled stages, retries/DLQ, idempotent loads, checkpointing, replayable raw zone, multi-AZ subnets for Glue/EMR/MSK |
| Backups | automated + manual snapshots, PITR (DynamoDB up to 35 d ~, RDS/Aurora), versioning, Object Lock, Backup Vault Lock ~ |
| Residency | restrict DR Regions to approved set (SCP) |

## 3. Regional vs global (and what is not global)
Global/control-plane: IAM, Route 53, CloudFront, AWS Organizations, (S3 bucket *names* are global but buckets are regional), Billing. **Regional**: S3 buckets, Glue Data Catalog, Lake Formation, KMS keys (multi-Region keys replicate explicitly), Kinesis, DynamoDB tables (global tables replicate), Redshift, Athena workgroups, Step Functions, EventBridge buses, Secrets Manager (replication optional), CloudTrail trails (multi-Region option). Many features are limited by Region (Glue 5.1 rollout, Athena capacity reservations unavailable in some Regions ✓, Kinesis on-demand limits differ by Region ✓, Firehose/MSK quotas by Region ✓, Lake Formation in NZ added Feb 2026 ✓ WN). Always check Region support when a stem names a Region.

## 4. Commonly tested quotas and numbers (see `cheatsheets/05-limits-and-numbers.md` for sources)
Kinesis shard 1 MB/s w, 2 MB/s r, 1,000 rec/s ✓ · record 10 MiB ✓ · retention 24 h–365 d ✓ · EFO 20/50 ✓ · Firehose buffer 60–900 s ✓, record 1,000 KiB ✓ · Lambda 15 min, 10,240 MB, 6 MB sync, 1,000 concurrency ✓ · SQS 1 MiB, 14 d, 12 h visibility ✓ · Step Functions Std 1 y / Express 5 min / 256 KiB / 25,000 events ✓ · S3 3,500/5,500 per prefix ✓ · Glacier min 90/90/180 d ✓ · DynamoDB 40,000 RCU/WCU table, 5 LSI, 20 GSI ✓ · Athena 1 M partitions scan, 262,144-byte query ✓ · MSK Serverless 200/400 MB/s, 5/10 MB/s per partition, 8 MiB message ✓ · Glue timeout max 7 d, retries ≤10 ✓ · KMS rotation default 365 d ✓ · CloudTrail Lake retention ≤ 3,653/2,557 d ✓ · Logs Insights 100 concurrent, 60-min timeout ✓.

## 5. Well-Architected principles applied to data analytics
- **Operational excellence**: IaC, CI/CD for pipelines, observability, runbooks, automated recovery, idempotent/replayable design.
- **Security**: least privilege, central governance (Lake Formation), encryption everywhere, data classification/masking, audit logs, private networking.
- **Reliability**: decouple, retry/DLQ, multi-AZ managed services, backups and tested restores, quotas awareness.
- **Performance efficiency**: right store/engine per access pattern, columnar + partitioning, caching/MVs, serverless scaling, data locality.
- **Cost optimisation**: tiering, right-sizing, serverless/commitments, query efficiency, lifecycle deletion.
- **Sustainability**: avoid duplicate copies, efficient formats, right-sized compute, delete stale data.
Data lens themes: define data tiers (raw/curated/consumption), catalog everything, govern centrally, automate quality, design for replay, separate storage and compute.

## 6. Decision shortcuts across domains
1. "Least operational overhead" → managed/serverless (Glue, Athena, Firehose, Step Functions, Lake Formation, EMR Serverless, Redshift Serverless, S3 Tables).
2. "Most cost-effective" → right tier/engine + columnar + commitment where steady + Spot/Flex where tolerant.
3. "Most secure" → LF/IAM least privilege + CMK + VPC endpoints + TLS enforced + auditing.
4. "Fastest / lowest latency" → in-memory/cache (MemoryDB, DAX ~), Express One Zone ✓, EFO ✓, provisioned capacity, co-located joins (KEY dist).
5. "Real time" → KDS/MSK + Flink/Lambda; "near real time" → Firehose (≥60 s ✓).
6. "Without moving/copying data" → Athena/Spectrum/federated query/Redshift data sharing/LF sharing/zero-ETL.
