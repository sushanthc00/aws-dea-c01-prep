# Mock Exam 2 — Part 2 Answers & Explanations (Q23–44)

### Q23 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.10 · Difficulty: Medium · Type: MC
- Correct B: FIFO preserves order within a message group and deduplicates; many groups allow parallelism.
- A: Standard queues provide at-least-once delivery with best-effort ordering.
- C: SNS standard does not guarantee order.
- D: Random partition keys destroy per-account ordering and one shard limits throughput.

### Q24 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.5 · Difficulty: Medium · Type: MC
- Correct C: Spectrum queries S3 data in place and joins it with local tables.
- A: Loading 200 TB is costly and unnecessary.
- B: Federated query targets RDS/Aurora databases, not S3 files.
- D: A migration service.

### Q25 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.4.3 · Difficulty: Medium · Type: MC
- Correct D: Crawlers infer one table per prefix layout; separating schemas gives correct tables.
- A: Frequency does not fix mixed schemas.
- B: Capacity is unrelated.
- C: Classifiers help determine format; disabling them does not resolve mixing.

### Q26 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.2 · Difficulty: Medium · Type: MC
- Correct A: Automatic rotation changes key material while keeping the key ID and ARN.
- B: Requires application changes.
- C: Gives up control.
- D: Deleting a key makes existing data undecryptable.

### Q27 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.2 · Difficulty: Hard · Type: MC
- Correct C: Idempotent writes make duplicate deliveries harmless.
- A: Does not affect duplicates.
- B: Does not affect duplicates.
- D: Risks data loss.

### Q28 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.1 · Difficulty: Medium · Type: MC
- Correct D: Provisioned (with auto scaling and reservations) is cheaper than on-demand for steady loads.
- A: On-demand is pricier for steady traffic.
- B: Pays for unused peak capacity.
- C: Wasteful.

### Q29 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.6 · Difficulty: Medium · Type: MC
- Correct A: Pipes connects a source (DynamoDB Streams) to a target with optional filtering and enrichment, without glue code.
- B: Database migration and replication.
- C: Delivery to storage destinations.
- D: File transfer.

### Q30 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.7 · Difficulty: Medium · Type: MC
- Correct B: Workgroups isolate teams and support scan limits and alerts.
- A: No per-team control.
- C: Storage tiering is unrelated.
- D: Redshift feature.

### Q31 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.1 · Difficulty: Medium · Type: MC
- Correct C: The Glue transform detects PII during processing and can redact or hash it.
- A: Manual and error-prone.
- B: Encryption does not remove or mask values.
- D: Macie discovers and reports in S3; it does not transform data.

### Q32 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.10 · Difficulty: Medium · Type: MC
- Correct D: Filter policies route messages by attributes to matching subscriptions.
- A: More producer logic.
- B: Code and operations.
- C: Scheduling service.

### Q33 — A, D

- Domain: D2 (Data Store Management) · Task/skill: 2.4.5 · Difficulty: Medium · Type: MR
- Correct A and D: Partition pruning and columnar large files reduce scanned data and overhead.
- B: Creates huge numbers of partitions and small files.
- C: Increases per-file overhead.
- E: Forces full scans.

### Q34 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct A: SQA and priorities let short queries bypass or outrank long ones.
- B: Table distribution does not fix queueing.
- C: Not relevant.
- D: Not relevant.

### Q35 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.8 · Difficulty: Medium · Type: MC
- Correct B: API Gateway plus Lambda gives a managed, secured API in front of Athena or cached results.
- A: Exposes the account.
- C: Not serverless.
- D: Public exposure.

### Q36 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.3.2 · Difficulty: Hard · Type: MC
- Correct C: Bulk is the cheapest tier and completes within about 5–12 hours.
- A: Fastest and most expensive (minutes).
- B: Faster than needed and costlier than Bulk.
- D: Not a Flexible Retrieval option.

### Q37 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.4 · Difficulty: Medium · Type: MC
- Correct B: Config evaluates configuration continuously and remediation actions can fix noncompliance.
- A: Detects unusual API activity.
- C: Finds sensitive data.
- D: Performance feature.

### Q38 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.9 · Difficulty: Medium · Type: MC
- Correct D: Batching and aggregation reduce request counts and handle bursts; retries with backoff absorb throttles.
- A: Lowers capacity.
- B: Does not address request rate.
- C: Complicates the design.

### Q39 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.3 · Difficulty: Medium · Type: MC
- Correct C: CloudWatch exposes disk usage metrics that can drive alarms.
- A: Records API calls.
- B: Evaluates configuration, not live usage.
- D: Unrelated to Redshift disk.

### Q40 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.4.2 · Difficulty: Medium · Type: MC
- Correct A: Adding a trailing column is a compatible schema change; old files simply yield NULL.
- B: Unnecessary.
- C: Loses data.
- D: Destructive.

### Q41 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.5 · Difficulty: Medium · Type: MC
- Correct B: EMR supports custom frameworks and applications such as HBase.
- A: Glue does not offer HBase.
- C: Not suitable for Spark clusters.
- D: Serverless SQL only.

### Q42 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.1 · Difficulty: Medium · Type: MC
- Correct C: Dynamic data masking returns masked values based on the user's role.
- A: A distribution setting.
- B: Performance feature.
- D: Queries S3.

### Q43 — B, D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MR
- Correct B and D: Hot shards come from skewed keys; better keys and more capacity spread load.
- A: Makes it worse.
- C: Removes resilience.
- E: Not related.

### Q44 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.3 · Difficulty: Medium · Type: MC
- Correct D: MemoryDB is a durable in-memory Redis-compatible database with multi-AZ transaction log.
- A: Single-digit millisecond, not Redis-compatible.
- B: Relational.
- C: MongoDB-compatible.
