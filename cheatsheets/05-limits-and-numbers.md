# Limits & numbers (verified 2026-10-20)
✓ = read on the cited official page today. ~ = widely documented but NOT re-fetched today (verified in Phase 5 or left flagged). Quotas change — exam tests *relationships* (e.g., per-shard limits) more than exact account defaults.

## Kinesis Data Streams ✓ [KDS quotas](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
| Item | Value |
|---|---|
| Provisioned shard write | **1 MB/s or 1,000 records/s** per shard |
| Provisioned shard read (shared, GetRecords) | **2 MB/s or 2,000 records/s** per shard; **5 GetRecords calls/s/shard**; ≤10,000 records or 10 MB per call |
| Record payload (pre-base64) | **up to 10 MiB** (burst capacity for intermittent 1–10 MiB records) — older material says 1 MB |
| PutRecords | ≤ 500 records, ≤ 10 MiB per request incl. partition keys |
| On-demand | new stream starts 4 MB/s write, 8 MB/s read; scales to 10 GB/s w / 20 GB/s r in us-east-1, us-west-2, eu-west-1; 200 MB/s w / 400 MB/s r other Regions; default 50 on-demand streams |
| Enhanced fan-out consumers | **20** per stream (standard); **50** with On-demand Advantage |
| Retention | min 24 h … max 365 d (8,760 h) |
| Mode switch | provisioned ↔ on-demand twice per 24 h |
| Shard iterator expiry | 5 min |
| Errors | `ProvisionedThroughputExceededException` on read when GetRecords returns 10 MB (wait 5 s) or insufficient throughput (1 s) |
| Shard math | shards = max( ceil(MB/s ÷ 1), ceil(records/s ÷ 1,000), ceil(consumer read MB/s ÷ 2) ) — EFO removes the shared-read term (each EFO consumer gets own pipe ~2 MB/s/shard ~) |
| Merge/Split | provisioned only (5 TPS) |

## Amazon Data Firehose ✓ [Firehose quotas](https://docs.aws.amazon.com/firehose/latest/dev/limits.html)
| Item | Value |
|---|---|
| Buffer interval hint | 60–900 s |
| Max record before base64 | 1,000 KiB; PutRecordBatch ≤ 500 records or 4 MiB |
| Direct PUT default (us-east-1/us-west-2/eu-west-1) | 500,000 records/s, 2,000 req/s, 5 MiB/s; other Regions 100,000 rec/s, 1,000 req/s, 1 MiB/s (auto-scales, adjustable); no cap when source = KDS |
| Retention if destination down | 24 h (DirectPut); KDS source → KDS retention |
| Dynamic partitioning | 500 active partitions/stream default; 1 GB/s per active partition |
| Redshift destination | only publicly accessible clusters; retry 0–7,200 s (also OpenSearch) |
| Lambda transform concurrency | 5 outstanding invocations per shard (S3/Redshift/OpenSearch); 10 Splunk |
| MSK source | 10 MB/s read per partition; 6 MB max record if Lambda enabled, 10 MB if not |
| Pricing quirk | ingestion billed per record rounded up to 5 KB → many tiny records cost more |

## Lambda ✓ [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
Memory 128–10,240 MB (1 vCPU at 1,769 MB) · timeout 900 s (15 min) · default concurrency 1,000/Region (raisable) · scaling 1,000 execution environments / 10 s per function · payload 6 MB sync, 1 MB async, 200 MB streamed response · /tmp 512–10,240 MB · env vars 4 KB · zip 50 MB zipped / 250 MB unzipped · container image 10 GB · layers 5 · sync invocation rate = 10 × concurrency · new accounts get reduced quotas.

## SQS ✓ [SQS message quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)
Message size **1 MiB** max (extended client → S3, 2 GB) · retention default 4 d, 60 s–14 d · visibility timeout default 30 s, max 12 h · delay 0–15 min · batch 10 · FIFO 300 TPS per API per partition (3,000 msg/s with batching); high-throughput FIFO up to 70,000 TPS (us-east-1/us-west-2/eu-west-1) non-batched · FIFO needs MessageGroupId.

## Step Functions ✓ [SFN quotas](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html)
| | Standard | Express |
|---|---|---|
| Max duration | **1 year** | **5 min** |
| History | 25,000 events/execution; kept 90 d | unlimited; needs CloudWatch Logs |
| Semantics | exactly-once workflow | at-least-once (async) / at-most-once (sync) ~ |
| Start rate | 1,300 burst / 300 per s refill (us-east-1/us-west-2/eu-west-1); 800/150 elsewhere | 6,000 |
| Input/output per state | 256 KiB | 256 KiB |
Distributed Map: ≤ 10,000 parallel child executions; redrive window 14 d (Standard).

## S3 ✓ [S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html), [lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html)
- **3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD per second per prefix**; no limit on prefixes → spread/parallelize. 503 Slow Down while scaling → retry with backoff.
- Lifecycle: objects **< 128 KB don't transition by default** (since Sep 2024; override with size filter). Min storage durations: **Glacier Instant Retrieval 90 d, Glacier Flexible 90 d, Deep Archive 180 d**; early deletion/transition → prorated charge. Glacier FR/DA add ~40 KB metadata overhead per object (8 KB at Standard rate + 32 KB at Glacier rate). Glacier FR → only Deep Archive via lifecycle; Deep Archive is one-way. Archived objects need restore (temp copy billed at Standard).
- Waterfall: Standard → IA / Intelligent-Tiering / One Zone-IA / GIR / GFR / GDA; IA → INT/ZIA/GIR/GFR/GDA; GIR → GFR/GDA; One Zone-IA → GFR/GDA.
- ~ Standard-IA/One Zone-IA: min 30 d storage; Standard → IA transition needs ≥30 d object age. ~ Glacier retrievals (Flexible): Expedited 1–5 min, Standard 3–5 h, Bulk 5–12 h; Deep Archive: Standard ≤12 h, Bulk ≤48 h. ~ PUT max 5 GB, object max 5 TB, multipart recommended > 100 MB.

## DynamoDB ✓ [DDB quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)
Per-table default 40,000 RCU/WCU (provisioned and on-demand) · per-account 80,000 provisioned · tables/Region 2,500 · **5 LSI, 20 GSI** default · ≤100 projected non-key attributes across indexes · Streams: ≤2 simultaneous readers per shard (1 for global tables) · provisioned decreases: 4 initially + 1/h (27/day) · import from S3 ≤50 concurrent jobs, 50,000 objects/job · full export ≤300 concurrent / 100 TB in flight.
~ Item 400 KB · partition 3,000 RCU/1,000 WCU · RCU = 4 KB strongly consistent (eventually consistent = half; transactional = 2×) · WCU = 1 KB · query/scan page 1 MB · LSI forces 10 GB per partition-key collection · TTL deletes within ~48 h of expiry (free, no WCU).

## Athena ✓ [Athena quotas](https://docs.aws.amazon.com/athena/latest/ug/service-limits.html)
Query string 262,144 bytes (hard) · DML timeout adjustable to 240 min (default 30 min ~) · active DML/DDL include queued; excess → `TooManyRequestsException` · reads ≤ **1 million partitions per scan** (tables may have 10 M) · 1,000 workgroups/Region · S3 buckets/account 10,000 default · Capacity reservations ✓: minimum 4 DPUs, queries on reserved capacity do not count toward DML/DDL quotas, queue up to 10 h, 20 workgroups per reservation, 100 reservations / 1,000 DPUs per account-Region (Athena capacity docs). The "1-minute minimum" in an earlier secondary source is [UNVERIFIED].

## Redshift (from What's New; ✓ headline-level)
Min TLS 1.2 enforced from 2026-01-31 · scalar Python UDF end of support after 2026-06-30 (use Lambda UDFs) · concurrency scaling covers KDS streaming-ingestion MV refresh (patch P203, Aug 2026) · Serverless 3-yr reservations up to 45 % savings.

## Glue (✓ headline) Glue 5.1: Spark 3.5.6, Python 3.11, Scala 2.12.18; Iceberg 1.10.0, Hudi 1.0.2, Delta 3.3.2.
## EMR (✓ headline) extended support through 2027-06-30 (5.36, 6.6–6.15) and 2027-08-31 (7.0–7.10).

## Not yet verified (do not memorise from here)
MSK broker/partition limits · KMS request rates (shared quota; SSE-KMS throttling on S3 — Bucket Keys reduce calls ~) · Glue DPU/worker sizes · MWAA environment classes · OpenSearch · Redshift node/cluster limits.
