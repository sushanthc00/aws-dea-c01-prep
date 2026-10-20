# Mock Exam 1 — Part 1 Answers & Explanations (Q1–22)

### Q1 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.10 · Difficulty: Medium · Type: MC
- Correct B: On-demand mode removes shard planning, and enhanced fan-out gives each registered consumer its own dedicated 2 MB/s per shard instead of sharing the 2 MB/s shared read limit.
- A: Shared throughput is 2 MB/s per shard across all consumers; three consumers of 18 MB/s need about 54 MB/s of read capacity but 18 shards give only 36 MB/s, and provisioned mode needs capacity planning.
- C: Firehose is a delivery service, not a multi-consumer replayable stream; it cannot feed three independent applications.
- D: One shared consumer group splits partitions between members instead of giving each application the full stream, and it migrates off Kinesis for no stated reason.

### Q2 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.3.2 · Difficulty: Medium · Type: MC
- Correct D: Glacier Instant Retrieval is built for rarely accessed data (about quarterly) that still needs millisecond access, at lower storage price than Standard-IA. Its 90-day minimum storage duration is satisfied by a 5-year retention.
- A: The Archive Access tiers need restore time (minutes to hours), so reads would not return in milliseconds.
- B: Glacier Flexible Retrieval requires a restore (minutes to hours) before reads.
- C: One Zone-IA is millisecond access but stores in a single AZ, which is a durability trade-off not asked for; Glacier Instant Retrieval is cheaper for quarterly access.

### Q3 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.7 · Difficulty: Medium · Type: MC
- Correct A: Bisecting the failed batch narrows it to the bad record; limiting retries and sending failure metadata to an SQS or SNS on-failure destination unblocks the shard.
- B: More shards do not change retry behavior; the failing shard still blocks.
- C: A longer timeout does not fix an exception thrown for a bad record.
- D: Enhanced fan-out changes read throughput, not error handling; the batch would still be retried.

### Q4 — B, D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.3 · Difficulty: Hard · Type: MR
- Correct B and D: Cross-account KMS use needs permission in the key policy (account A) and in an identity policy of the principal in account B.
- A: AWS managed keys cannot be shared across accounts, and re-encryption is unnecessary.
- C: Grants are created on the key in the key's account; the S3 service principal in account B is not the issue.
- E: Rotation does not affect authorization.

### Q5 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.4.5 · Difficulty: Medium · Type: MC
- Correct C: The problem is data skew. Salting spreads the hot key across many partitions so work is distributed evenly.
- A: More workers do not help if one partition holds most of the data.
- B: Bookmarks control incremental reads, not skew.
- D: Flex changes cost and start behavior, not data distribution.

### Q6 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.1 · Difficulty: Medium · Type: MC
- Correct D: Step Functions natively orchestrates Glue, Athena, and Lambda with Retry/Catch and no servers to manage.
- A: MWAA works but runs an always-on environment that must be sized and maintained.
- B: Glue workflows only chain Glue crawlers and jobs, not Athena queries or Lambda.
- C: Rules react to events but do not provide state, retries with backoff, or branching.

### Q7 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.4.1 · Difficulty: Medium · Type: MC
- Correct A: Matching distribution keys co-locate rows with the same customer_id on the same slice, avoiding redistribution.
- B: ALL replicates the table to every node; 500 million rows is far too large to replicate.
- C: EVEN spreads rows round-robin, which forces redistribution for joins.
- D: Replicating a 2-billion-row table is wasteful and slows loads.

### Q8 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.5 · Difficulty: Medium · Type: MC
- Correct C: Glue is serverless Spark with JDBC connections, scheduling, and Parquet output.
- A: Lambda has a 15-minute limit and 10 GB memory ceiling; 2 TB of Spark-style processing does not fit.
- B: EMR on EC2 works but requires cluster management.
- D: Athena cannot run custom PySpark logic (Athena Spark notebooks are interactive and not the best fit for a scheduled production ETL).

### Q9 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct B: Columnar compressed format plus partition pruning cuts bytes scanned, which drives both cost and speed.
- A: A longer timeout does not reduce data scanned.
- C: More prefixes do not reduce the bytes read by a full scan.
- D: Result reuse only helps repeated identical queries.

### Q10 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.4 · Difficulty: Medium · Type: MC
- Correct D: Lake Formation provides column-level permissions enforced for Athena, centrally managed and logged.
- A: Bucket policies work on objects, not columns.
- B: Denying GetTable blocks the whole table, not one column.
- C: Works but adds a pipeline and duplicate storage to maintain.

### Q11 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Medium · Type: MC
- Correct A: MSK is managed Apache Kafka, compatible with Kafka APIs, Streams, and Connect (MSK Connect).
- B: Kinesis uses its own APIs; applications would need rewriting.
- C: Firehose is delivery only.
- D: SQS is a queue with a different API.

### Q12 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.4.1 · Difficulty: Medium · Type: MC
- Correct B: The base table serves pattern 1 with a Query; the GSI serves pattern 2.
- A: A local secondary index must share the table partition key, so it cannot re-partition by customerId.
- C: Scans read the whole table and are inefficient.
- D: Date as a partition key creates hot partitions and does not support either pattern well.

### Q13 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.6 · Difficulty: Medium · Type: MC
- Correct D: Firehose buffers and converts JSON to Parquet or ORC using a Glue Data Catalog schema, fully managed.
- A: Requires custom code and operations.
- B: Works but needs cluster management.
- C: Crawlers infer schemas; they do not move or convert streaming data.

### Q14 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct A: Concurrency scaling adds transient capacity for bursts of concurrent queries and is billed only when used; automatic WLM manages queues.
- B: Permanent capacity for a short burst is expensive.
- C: DISTSTYLE ALL does not address concurrency and bloats storage.
- D: RDS is not designed for analytical workloads of this kind.

### Q15 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.9 · Difficulty: Medium · Type: MC
- Correct C: On-demand adapts to unpredictable write bursts without capacity planning; SDK retries with backoff handle residual throttling.
- A: The problem is writes, not reads.
- B: DAX is a read cache and does not help writes.
- D: An index adds write cost.

### Q16 — A, D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.7 · Difficulty: Medium · Type: MR
- Correct A and D: Iceberg supports transactional row-level changes and snapshot time travel.
- B: Iceberg uses metadata and file statistics, not B-tree indexes.
- C: Iceberg tables still need a catalog.
- E: Iceberg has no enforced foreign keys.

### Q17 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.3 · Difficulty: Medium · Type: MC
- Correct B: Secrets Manager supports scheduled automatic rotation for RDS and Glue connections can read the secret.
- A: Manual and error-prone.
- C: No rotation capability.
- D: Poor practice and requires changes.

### Q18 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.6 · Difficulty: Medium · Type: MC
- Correct D: Event-driven start with orchestrated ordered steps and no polling.
- A: Delay of up to an hour and runs even without a file.
- B: Polling wastes invocations and needs de-duplication logic.
- C: Crawlers do not run continuously and do not run jobs.

### Q19 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.3 · Difficulty: Medium · Type: MC
- Correct B: Iterator age measures how old the oldest record returned is; rising age means the consumer is lagging.
- A: Indicates producer-side write throttling.
- C: Measures ingest volume, not consumer lag.
- D: CloudTrail does not alert on lag and GetRecords is a data-plane call.

### Q20 — C, E

- Domain: D2 (Data Store Management) · Task/skill: 2.3.1 · Difficulty: Medium · Type: MR
- Correct C and E: Offload cold data to cheap S3 in a columnar format and keep it queryable with Spectrum.
- A: Raises cost.
- B: Does not reduce storage.
- D: Removes the data, so it is no longer queryable.

### Q21 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.2 · Difficulty: Hard · Type: MC
- Correct B: Limiting concurrent invocations bounds database connections; RDS Proxy pools and reuses them.
- A: More memory does not limit concurrency.
- C: FIFO ordering is unrelated and could lower throughput.
- D: Visibility timeout controls reprocessing, not concurrency.

### Q22 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.1 · Difficulty: Medium · Type: MC
- Correct A: Gateway endpoints for S3 are free and keep traffic on the AWS network.
- B: Works but incurs hourly and data-processing charges.
- C: Private subnets would still lack a route, and it exposes traffic to the internet path.
- D: Does not provide S3 access.
