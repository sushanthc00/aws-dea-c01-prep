# Which service when — master decision tree
Tags: ✓ numbers verified (see 05-limits) · ~ standard AWS behaviour, to be re-checked in Phase 3/5. Qualifier words decide: **least operational overhead** → serverless/managed; **most cost-effective** → right-size, columnar, tiering, batch over streaming; **near real time** → Firehose (≥60 s buffer ✓) ; **real time / sub-second** → KDS/MSK + Flink/Lambda.

## 1. Ingestion
```
Streaming?
├─ Just land in S3/Redshift/OpenSearch/Iceberg/HTTP, minimal code, ≥60 s latency OK → Data Firehose (formerly Kinesis Data Firehose)
├─ Custom consumers, replay, ordering per key, multiple apps → Kinesis Data Streams
│     ├─ unpredictable traffic, no capacity planning → on-demand
│     └─ steady, cost-optimise → provisioned
├─ Kafka API / existing Kafka apps / MirrorMaker / Kafka Connect → Amazon MSK (Serverless if bursty ~)
├─ Windowed aggregation, joins, CEP, exactly-once stateful → Managed Service for Apache Flink (was Kinesis Data Analytics)
├─ Decoupled work queue, per-message ack, DLQ → SQS  (ordered/dedup → FIFO)
├─ Pub/sub fan-out to many subscribers → SNS (+SQS fan-out)
└─ Event routing/filtering from AWS/SaaS, schedule → EventBridge (Pipes for source→filter→enrich→target ~)
Batch / DB / files?
├─ DB → AWS: DMS (full load + CDC)  [schema conversion: DMS Schema Conversion; SCT out of scope list]
├─ Files on-prem ↔ S3/EFS/FSx online, scheduled, verified → DataSync
├─ SFTP/FTPS/FTP/AS2 into S3/EFS, partners → Transfer Family
├─ Petabytes, poor network → Snow Family
├─ SaaS (Salesforce, SAP, ServiceNow…) → AppFlow  (zero-ETL for supported SaaS/DB sources ~)
├─ Aurora/RDS/DynamoDB → Redshift or lakehouse with no pipeline → zero-ETL integration
└─ REST API pull on schedule → Lambda/Glue (python shell) + EventBridge Scheduler; expose data via API Gateway/Lambda/Athena
```

## 2. Transformation engine
| Need | Pick | Why / why not |
|---|---|---|
| Serverless Spark ETL, catalog-integrated, bookmarks | **Glue** | least ops; DPU-hour billing; min 1-min billing ~ |
| Large/custom Spark/Hive/Presto/HBase, tuning, spot, existing Hadoop | **EMR** (EC2 / EKS / Serverless) | control & cost at scale; more ops (Serverless reduces) |
| Small event-driven (<15 min ✓, ≤10 GB memory ✓) | **Lambda** | cheapest for light work |
| SQL ELT on data already in S3 | **Athena** (CTAS/INSERT, UNLOAD) | no infra; pay per TB scanned |
| SQL ELT inside warehouse | **Redshift** (INSERT/MERGE, MVs, stored procs) | joins/aggregates at scale |
| No-code profiling/cleaning | **DataBrew** (250+ transforms ~) | analysts; not for heavy ETL |
| Real-time stateful | **Flink** | |
| Container batch | **AWS Batch / ECS / EKS** | when custom runtimes |

## 3. Analytics/query
| Need | Pick |
|---|---|
| Ad-hoc SQL on S3, infrequent | **Athena** |
| Repeated BI/dashboards, complex joins, high concurrency | **Redshift** (+ Spectrum for cold S3) |
| Big-data frameworks, ML prep, Spark at scale | **EMR** |
| Full-text search, log analytics, dashboards | **OpenSearch** |
| BI | **Amazon Quick (QuickSight)** — SPICE (in-memory import) vs direct query |
| Governed lakehouse (SQL + Spark + ML, one catalog) | SageMaker Unified Studio / Lakehouse (Iceberg) |

## 4. Operational / serving stores
| Workload | Pick |
|---|---|
| Key-value/doc, single-digit ms, huge scale, access patterns known | **DynamoDB** (DAX for µs reads ~) |
| Relational OLTP, joins, existing engine | **RDS** ; cloud-native scale/HA/read replicas, pgvector → **Aurora** |
| Cassandra-compatible serverless | **Keyspaces** |
| MongoDB-compatible | **DocumentDB** |
| Graph traversals (relationships) | **Neptune** |
| Durable in-memory, Redis-compatible, microsecond reads | **MemoryDB** (primary DB) |
| Time series | Timestream — **not in current scope lists** ✓ ; know only "time-series DB" |
| Vector similarity | Aurora PostgreSQL pgvector (HNSW/IVF), OpenSearch, MemoryDB vector, S3 Vectors, Bedrock Knowledge Bases (managed RAG) ~ |
| Data warehouse | **Redshift** |
| Object lake | **S3** (+ S3 Tables for managed Iceberg ✓ in scope) |

## 5. Orchestration
| | Use when |
|---|---|
| **Step Functions** | AWS-native serverless, visual, branching, retries/catch, direct SDK integrations; Standard (≤1 y ✓) vs Express (≤5 min ✓, high-rate) |
| **MWAA** | Existing Airflow DAGs, rich scheduling, Python; always-on cost |
| **Glue Workflows/triggers** | Glue-only crawler→job chains |
| **EventBridge (rules/Scheduler)** | Event triggers & cron; not multi-step state |
| **Lambda** | Glue code for single steps only |

## 6. Migration/transfer quick map
DMS = database migration/CDC · DataSync = bulk file transfer & sync · Transfer Family = managed SFTP/FTPS/FTP/AS2 endpoint to S3/EFS · Snow = offline bulk · AppFlow = SaaS↔AWS · Application Migration Service = servers (lift-and-shift) · Data Exchange = third-party data subscriptions.

## 7. Governance
Identity-based IAM → coarse; **Lake Formation** → fine-grained (table/column/row/cell, LF-tags) across Athena, Redshift Spectrum, EMR, Glue ✓ (exam guide 4.2.4) ; bucket policies/Access Points → S3-level; Macie → find PII in S3; Redshift data sharing → live cross-cluster share; SageMaker Catalog/DataZone → business catalog, projects, subscriptions; Config → config history; CloudTrail (+Lake) → API audit.
