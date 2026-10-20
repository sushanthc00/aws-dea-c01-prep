# Streaming: Kinesis Data Streams · Data Firehose · MSK · Flink · SQS/SNS/EventBridge
✓ = verified (05-limits) · ~ = to re-check.

## Comparison
| | KDS | Firehose | MSK | SQS | SNS | EventBridge |
|---|---|---|---|---|---|---|
| Model | ordered log, shards | managed delivery | Kafka log, partitions | queue | pub/sub | event bus/rules |
| Replay | **Yes** (24 h–365 d ✓) | No | Yes (retention config) | No (once deleted) | No | Archive/replay feature ~ |
| Consumers | many (shared 2 MB/s/shard ✓; EFO 20/50 ✓) | none (destinations) | many consumer groups | competing consumers | many subscribers | many targets |
| Ordering | per partition key/shard | n/a | per partition | FIFO only (group ID ✓) | FIFO topics ~ | none guaranteed |
| Latency | ~70–200 ms (EFO ~70 ms ~) | ≥ 60 s buffer ✓ (zero-buffering option exists ~) | ms | ms | ms | sec |
| Ops | capacity (provisioned) or on-demand | none | cluster/serverless | none | none | none |
| Destinations | Lambda, Flink, KCL, Firehose | S3, Redshift*, OpenSearch, Splunk, HTTP, Snowflake, Iceberg ~ | Connect sinks, Flink, Lambda | Lambda, EC2.. | SQS, Lambda, HTTP, Firehose… | 20+ targets |
*Redshift only publicly accessible clusters ✓.

## Keyword → answer
- "replay / reprocess / multiple independent consumers" → **KDS** (or MSK).
- "load into S3/Redshift with no code / convert to Parquet / near real time / buffering" → **Firehose** (format conversion needs Glue table schema ~).
- "Kafka / open-source / lift existing Kafka" → **MSK**.
- "windowing, sliding/tumbling, real-time aggregation" → **Managed Service for Apache Flink** (old name Kinesis Data Analytics — still appears in old material).
- "decouple, retry, DLQ, back-pressure" → **SQS**; "fan-out one event to many" → **SNS → SQS**.
- "react to AWS/SaaS events, content-based filtering, schedule" → **EventBridge**.
- "CDC from DynamoDB" → **DynamoDB Streams** (24 h retention ~; ≤2 readers/shard ✓) or **Kinesis Data Streams for DynamoDB** (longer retention, multiple consumers).
- "database change data capture to stream/lake" → **DMS** (targets: Kinesis, MSK, S3, Redshift).
- "ordering per entity" → partition key = entity ID (KDS/MSK); FIFO + MessageGroupId (SQS).

## KDS operations
- Hot shard: skewed partition key → add randomness/salt, use more distinct keys; `WriteProvisionedThroughputExceeded` → producer retries w/ backoff, batch (PutRecords ≤500 ✓), KPL aggregation, add shards (UpdateShardCount / split) or switch to on-demand.
- Read throttling (`ReadProvisionedThroughputExceeded`): too many shared consumers → **enhanced fan-out**; or increase shards; 5 GetRecords/s/shard ✓.
- Consumer lag metric: `GetRecords.IteratorAgeMilliseconds` (rising = consumer too slow; Lambda: raise batch size/parallelization factor (1–10 ~), bisect batch on error, on-failure destination, tumbling window ~). Lambda ESM polls each shard; failed batch blocks shard until success/expiry (poison pill).
- KCL: one lease per shard in DynamoDB table; checkpointing; workers ≤ shards.
- Encryption: SSE-KMS (stream) ; TLS in transit; VPC endpoint (interface) available ~.
- Producer options: SDK PutRecord(s), **KPL** (aggregation/collection, async), Kinesis Agent, Firehose-from-KDS.
- On-demand vs provisioned: on-demand = no planning, scales to 2× previous peak in ~15 min? ~[UNVERIFIED]; use provisioned for steady predictable cost-optimised loads.

## Firehose operations
- Buffer size/interval (60–900 s ✓): flush when first hit. Larger → fewer, larger S3 files (good for Athena).
- Transform with Lambda (5 concurrent invocations per shard ✓); failed records → S3 error prefix; source backup option ~.
- Dynamic partitioning (500 active partitions ✓) → S3 prefixes by key; data format conversion JSON→Parquet/ORC ~.
- Delivery failure retry/backup to S3; DirectPut buffering 24 h ✓.
- Source can be: Direct PUT, KDS, MSK, CloudWatch Logs/EventBridge/IoT etc. ~

## MSK
- Provisioned (brokers across 3 AZs ~; EBS storage, tiered storage ~) vs Serverless (auto capacity). MSK Connect = managed Kafka Connect. Auth: IAM, SASL/SCRAM (Secrets Manager), mTLS ~. Encryption in transit TLS, at rest KMS ~. Partition count caps parallelism; `kafka-topics` etc. Lag → add consumers ≤ partitions.
- Firehose can read from MSK ✓ (10 MB/s per partition ✓).

## Flink (Managed Service for Apache Flink)
Stateful stream processing, event-time windows, checkpoints/snapshots for exactly-once ~, Flink SQL/DataStream/Table API/Python; sources KDS/MSK/S3; sinks S3, Firehose, OpenSearch, DynamoDB etc. Autoscaling KPUs ~. Studio notebooks (Zeppelin) ~.

## Stateful vs stateless (skill 1.1.12)
Stateless: each record independent (filter/map; Lambda per record). Stateful: needs memory across records (windows, aggregation, joins, dedupe) → Flink/Spark Structured Streaming, state in checkpointed store; idempotency for replays.

## Replayability (1.1.11)
Keep immutable raw zone in S3; KDS/MSK retention; idempotent writes (MERGE/upsert, dedupe key); Glue job bookmarks reset; Iceberg snapshots/time travel; EventBridge archive; SQS can't replay → DLQ redrive only.

## Throttling & rate limits (1.1.9)
Exponential backoff + jitter; SDK retries; batch writes; DynamoDB on-demand/auto scaling & partition key design; RDS: connection pool/RDS Proxy ~, read replicas; Kinesis: shards/EFO/batching; Lambda: reserved concurrency to protect downstream, SQS as buffer (batch size, max concurrency on ESM ~).

## Fan-in / fan-out (1.1.10)
Fan-in: many producers → one stream (KPL, agents, partition keys). Fan-out: KDS EFO ✓, SNS→SQS, EventBridge targets, Firehose from KDS (one stream feeding S3 + Lambda + Flink).
