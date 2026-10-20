# Mock Exam 1 — Part 2 Answers & Explanations (Q23–44)

### Q23 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.3 · Difficulty: Medium · Type: MC
- Correct C: Bookmarks persist processing state; they only work when the job is initialized, sources carry transformation_ctx, and the job commits.
- A: More capacity does not prevent reprocessing.
- B: Crawlers update the catalog, they do not track which files a job processed.
- D: S3 Select filters within an object and does not track processed files.

### Q24 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.2.4 · Difficulty: Medium · Type: MC
- Correct A: With partition projection Athena computes partitions from table properties, so no catalog registration or crawler is needed for predictable patterns.
- B: Costly and still delayed.
- C: Works but adds scheduled operations and scans all prefixes.
- D: Increases data scanned and cost.

### Q25 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.6 · Difficulty: Hard · Type: MC
- Correct D: Distributed Map runs child executions in parallel, each with its own history, avoiding the parent's 25,000-event limit.
- A: Express workflows are limited to 5 minutes.
- B: The execution history limit is a hard quota.
- C: Timeouts are not the cause.

### Q26 — A, C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.2 · Difficulty: Medium · Type: MR
- Correct A and C: Macie discovers sensitive data; Lake Formation tag-based access control restricts column access in Athena.
- B: GuardDuty detects threats, not PII.
- D: Versioning protects against overwrites, not access.
- E: Encryption config does not control column visibility.

### Q27 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Hard · Type: MC
- Correct B: Redshift streaming ingestion queries the stream through an external schema and materialized view, with no pipeline code.
- A: Firehose supports only publicly accessible Redshift clusters.
- C: Row-by-row inserts are slow, costly, and need code.
- D: DMS does not read from Kinesis as a source.

### Q28 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.5 · Difficulty: Medium · Type: MC
- Correct D: Zero-ETL replicates data continuously into Redshift without pipelines to maintain.
- A: Works but must be built and operated.
- B: Batch micro-ETL with operational burden.
- C: Not a supported pattern and fragile.

### Q29 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.7 · Difficulty: Hard · Type: MC
- Correct A: EFS gives a shared, updatable file system that all invocations can mount.
- B: ZIP limit is 250 MB unzipped and changing data requires redeploy.
- C: Layers count toward the 250 MB limit and are versioned artifacts.
- D: Environment variables are limited to 4 KB.

### Q30 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.1 · Difficulty: Medium · Type: MC
- Correct C: SPICE caches data in memory for fast dashboards and avoids repeated Athena scans.
- A: Workgroups do not add compute.
- B: Timeout is not the issue.
- D: Does not address repeated scans.

### Q31 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.4.3 · Difficulty: Medium · Type: MC
- Correct B: Heterogeneous migration needs schema conversion; DMS full load plus change data capture minimizes downtime.
- A: DataSync copies files, not database content.
- C: Offline transfer with long downtime.
- D: Crawlers catalog data, they do not migrate it.

### Q32 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.1 · Difficulty: Medium · Type: MC
- Correct A: Redshift data sharing provides live read access across accounts without copying.
- B: Creates copies and delay.
- C: Does not grant table access.
- D: Creates a stale copy.

### Q33 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.10 · Difficulty: Medium · Type: MC
- Correct D: SNS fan-out to SQS gives independent buffering, retries, and DLQs per consumer.
- A: Consumers would compete for messages.
- B: Coupled failure and retry behavior.
- C: Extra producer complexity and no DLQ semantics.

### Q34 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.5 · Difficulty: Medium · Type: MC
- Correct B: Object-level API calls such as DeleteObject are data events that must be explicitly enabled.
- A: Server access logs are best-effort and harder to attribute to IAM principals.
- C: Insights detects unusual management activity.
- D: Config records configuration changes, not object deletes.

### Q35 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.3.4 · Difficulty: Easy · Type: MC
- Correct C: TTL deletes expired items in the background without consuming write capacity.
- A: Scans and deletes consume capacity and operations effort.
- B: Streams capture changes, they do not expire items.
- D: S3 lifecycle does not apply to DynamoDB.

### Q36 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.5 · Difficulty: Medium · Type: MC
- Correct A: Flink provides event-time windows, state, and checkpointed exactly-once processing.
- B: Firehose buffers and delivers; it does not compute windowed aggregates.
- C: Per-record Lambda is stateless and cannot easily maintain windows.
- D: Batch, not real time.

### Q37 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.2 · Difficulty: Easy · Type: MC
- Correct D: Standard parameters are free and SecureString encrypts with KMS; rotation is not needed.
- A: Charged per secret; rotation not required.
- B: Not a secrets store with fine-grained API access.
- C: Over-engineered.

### Q38 — B, E

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.8 · Difficulty: Medium · Type: MR
- Correct B and E: Logs Insights handles quick queries; S3 plus Athena is the low-cost long-term analysis path.
- A: Operationally heavy and unsuited.
- C: Manual and costly.
- D: X-Ray is out of exam scope and traces requests, not log analysis.

### Q39 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.11 · Difficulty: Medium · Type: MC
- Correct C: A replayable raw layer plus idempotent loads allows safe reprocessing.
- A: Firehose does not provide replay storage.
- B: Removes the ability to reprocess.
- D: Loses the original data.

### Q40 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.4.5 · Difficulty: Medium · Type: MC
- Correct A: Too many partitions and small files increase metadata and request overhead; coarser partitions and larger columnar files fix both.
- B: Makes it worse.
- C: Row text is slower to scan.
- D: Workgroups do not change planning cost.

### Q41 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Hard · Type: MC
- Correct D: The lock views identify the blocker; terminating the backend releases the lock.
- A: Queues do not release locks.
- B: VACUUM would also wait for the lock.
- C: Resizing does not resolve a lock conflict.

### Q42 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.9 · Difficulty: Hard · Type: MC
- Correct B: SQS buffers bursts and concurrency limiting plus backoff keeps calls within the rate.
- A: Would trigger throttling.
- C: Ignores the limit and needs servers.
- D: Heavy and unnecessary.

### Q43 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.3 · Difficulty: Hard · Type: MC
- Correct C: SCPs are preventive guardrails across accounts and can condition on the requested Region.
- A: Replication copies data to other Regions.
- B: Boundaries apply per principal and are harder to enforce centrally.
- D: Config is detective, not preventive.

### Q44 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.8 · Difficulty: Hard · Type: MC
- Correct D: HNSW offers high recall and fast approximate nearest-neighbor search at the cost of memory and build time.
- A: B-tree cannot do vector similarity search.
- B: GIN supports full-text and array containment, not similarity.
- C: IVFFlat builds faster and uses less memory but typically has lower recall and needs representative data to build.
