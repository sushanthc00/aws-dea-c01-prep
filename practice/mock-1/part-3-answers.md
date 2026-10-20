# Mock Exam 1 — Part 3 Answers & Explanations (Q45–65)

### Q45 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.2 · Difficulty: Medium · Type: MC
- Correct C: Provisioned concurrency keeps execution environments initialized, and scheduled scaling matches the predictable peak.
- A: Timeout does not affect cold-start time.
- B: Limits concurrency and would throttle.
- D: Layers do not remove initialization time.

### Q46 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.1.1 · Difficulty: Medium · Type: MC
- Correct A: Keyspaces is Cassandra-compatible and serverless.
- B: DocumentDB is MongoDB-compatible.
- C: Neptune is a graph database.
- D: MemoryDB is a Redis-compatible in-memory database.

### Q47 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.4.1 · Difficulty: Medium · Type: MC
- Correct C: Glue Data Quality evaluates rules during processing and can fail the job so publication stops.
- A: Crawlers infer schema, not validate quality.
- B: Bookmarks track progress.
- D: Capacity does not validate data.

### Q48 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.1 · Difficulty: Medium · Type: MC
- Correct D: MWAA runs Airflow DAGs with little modification and managed infrastructure.
- A: Requires rewriting DAGs into state machine definitions.
- B: Only orchestrates Glue components.
- C: Schedules invocations but is not a DAG engine.

### Q49 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.5 · Difficulty: Medium · Type: MC
- Correct B: Kinesis is accessed privately through an interface endpoint.
- A: Gateway endpoints exist only for S3 and DynamoDB.
- C: Would expose traffic to the internet path and requires routes and public addressing.
- D: Not needed for service access inside a VPC.

### Q50 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.7 · Difficulty: Medium · Type: MC
- Correct C: S3 Tables is purpose-built managed Iceberg storage with automatic table maintenance.
- A: Works but requires building and operating maintenance.
- B: Plain files, not a managed table format.
- D: A key-value store, not an analytic table format.

### Q51 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.7 · Difficulty: Medium · Type: MC
- Correct A: Gzip is not splittable, so one file means one task; multiple files or a splittable columnar format restores parallelism.
- B: Extra workers sit idle.
- C: Compression level does not change splittability.
- D: The bottleneck is parallelism, not driver memory.

### Q52 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct B: COPY loads files in parallel across slices; one file means no parallelism.
- A: Bigger nodes do not parallelize a single file.
- C: INSERT is far slower for bulk loads.
- D: Not related to load parallelism.

### Q53 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.2 · Difficulty: Medium · Type: MC
- Correct D: Bucket Keys reduce calls from S3 to KMS, lowering cost and throttling.
- A: Moves key management to clients.
- B: Aliases map to one key at a time; not a fix.
- C: Violates security requirements.

### Q54 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.3.3 · Difficulty: Medium · Type: MC
- Correct B: Noncurrent version expiration removes old versions while keeping current objects.
- A: Versioning cannot be removed once enabled (only suspended) and would drop protection.
- C: Prevents deletion.
- D: Adds copies and cost.

### Q55 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.5 · Difficulty: Medium · Type: MC
- Correct A: EventBridge Scheduler supports time zones natively.
- B: EventBridge rule cron expressions are evaluated in UTC.
- C: Extra code to maintain.
- D: Requires servers.

### Q56 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.7 · Difficulty: Medium · Type: MC
- Correct C: Capacity reservations give dedicated query capacity and control concurrency for predictable heavy workloads.
- A: Timeout does not affect admission.
- B: Not the limiting factor.
- D: Slower and more costly.

### Q57 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.6 · Difficulty: Medium · Type: MC
- Correct A: Scoped actions and resource ARNs limit access to what the job needs.
- B: s3:* on all resources grants every S3 action on every bucket.
- C: AmazonS3FullAccess allows all S3 actions on all buckets.
- D: AdministratorAccess grants every action on every service.

### Q58 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.2 · Difficulty: Easy · Type: MC
- Correct D: AppFlow provides managed SaaS connectors including Salesforce with scheduling.
- A: DataSync moves files between storage systems.
- B: Offline appliance for bulk data.
- C: SFTP/FTPS endpoints.

### Q59 — A, C

- Domain: D2 (Data Store Management) · Task/skill: 2.4.1 · Difficulty: Hard · Type: MR
- Correct A and C: Spread access with better keys or sharded keys.
- B: DAX is a read cache; writes still hit the table.
- D: Indexes add write cost without spreading load.
- E: Writes are the issue.

### Q60 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.6 · Difficulty: Medium · Type: MC
- Correct D: A window frame of the current row and the six preceding rows yields a rolling 7-day average per store.
- A: Produces one overall average per store.
- B: Ranking, not averaging.
- C: Not valid Athena syntax and unrelated.

### Q61 — A, C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.4 · Difficulty: Medium · Type: MR
- Correct A and C: TLS is enforced with the SecureTransport condition; default encryption protects data at rest.
- B: Speeds transfers; not an encryption control.
- D: Protects deletes.
- E: Billing setting.

### Q62 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Hard · Type: MC
- Correct B: Glue streaming jobs read from Kinesis and process micro-batches serverlessly, including writes to Iceberg.
- A: A scheduler is clumsy and has start-up overhead.
- C: Athena does not read directly from Kinesis.
- D: Not suited to Spark micro-batch transforms.

### Q63 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.2.6 · Difficulty: Medium · Type: MC
- Correct A: SageMaker Catalog provides business metadata, publishing and subscription governance, and lineage.
- B: Technical metadata only.
- C: Records API activity.
- D: Records configuration state.

### Q64 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.3 · Difficulty: Medium · Type: MC
- Correct C: Glue emits job state change events that EventBridge can route to SNS.
- A: Delayed and manual.
- B: Manual.
- D: Insights detects unusual API activity, not job state.

### Q65 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.1 · Difficulty: Medium · Type: MC
- Correct D: Neptune is a graph database optimized for relationship traversals.
- A: Key-value access patterns, poor for deep traversals.
- B: Analytical warehouse with expensive multi-hop joins.
- C: Document store, not graph traversal.
