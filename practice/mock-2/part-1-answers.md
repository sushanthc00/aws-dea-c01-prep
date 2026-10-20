# Mock Exam 2 — Part 1 Answers & Explanations (Q1–22)

### Q1 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.6 · Difficulty: Medium · Type: MC
- Correct C: Dynamic partitioning extracts keys from records (inline parsing or Lambda) and writes to key-based prefixes.
- A: Many small objects and custom code.
- B: Adds latency and a second pipeline.
- D: Does not scale and hits stream quotas.

### Q2 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Hard · Type: MC
- Correct A: Each shard accepts up to 1,000 records/s and 1 MB/s. Records require 6,000 / 1,000 = 6 shards; bytes require 3 shards. The larger value (6) governs.
- B: Considers only the 1 MB/s limit.
- C: Over-provisioned for these numbers.
- D: Below both limits.

### Q3 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.3.2 · Difficulty: Medium · Type: MC
- Correct D: Intelligent-Tiering moves objects between access tiers automatically based on usage without retrieval fees.
- A: Needs restores and delays access.
- B: Single-AZ and charges retrieval fees.
- C: Charges retrieval fees; wrong if objects are hot again.

### Q4 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.1 · Difficulty: Hard · Type: MC
- Correct B: Cross-account access requires an allow on both sides: the identity policy in A and the resource policy (bucket policy) in B.
- A: The role is the principal, not the service principal.
- C: Unnecessary long-term credentials.
- D: Irrelevant.

### Q5 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct A: Reserved concurrency guarantees capacity for that function (and caps it).
- B: Memory does not provide concurrency.
- C: A longer timeout would hold concurrency longer.
- D: VPC placement does not change concurrency.

### Q6 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.3 · Difficulty: Medium · Type: MC
- Correct D: Express workflows support very high start rates, run up to 5 minutes, and are priced for high-volume short executions.
- A: Per-state-transition pricing is costly at this volume and start rates are lower.
- B: Intended for large batch fan-out, not high-rate events.
- C: Not a general event workflow engine.

### Q7 — B, E

- Domain: D2 (Data Store Management) · Task/skill: 2.4.1 · Difficulty: Medium · Type: MR
- Correct B and E: A sort key on the date allows zone maps to skip blocks; a materialized view precomputes the repeated aggregation.
- A: Replicates a large table to every node.
- C: Interleaved keys on all columns dilute pruning and slow loads.
- D: Reduces performance.

### Q8 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Medium · Type: MC
- Correct B: DMS supports ongoing replication to S3 and can write Parquet.
- A: Custom and not incremental.
- C: Requires cluster management.
- D: DataSync copies files, not database changes.

### Q9 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.6 · Difficulty: Medium · Type: MC
- Correct C: Core nodes hold HDFS data and the primary coordinates, so keep them On-Demand; task nodes are stateless and cheap on Spot.
- A: Spot loss of core nodes risks data loss and cluster failure.
- B: Works but costs more.
- D: No scale or resilience.

### Q10 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.2.5 · Difficulty: Medium · Type: MC
- Correct A: Glue connections define network access to JDBC sources; crawlers use them to read schemas.
- B: Irrelevant to JDBC sources.
- C: Irrelevant.
- D: Tags govern permissions, not connectivity.

### Q11 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.7 · Difficulty: Medium · Type: MC
- Correct B: A higher parallelization factor processes multiple batches per shard concurrently while preserving per-key ordering.
- A: Memory does not add parallelism.
- C: Batching improves efficiency.
- D: Lowers throughput.

### Q12 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.3 · Difficulty: Medium · Type: MC
- Correct C: Role-based grants apply least privilege and scale to groups.
- A: Excessive.
- B: Exposes data broadly.
- D: A security violation.

### Q13 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.1 · Difficulty: Medium · Type: MC
- Correct A: Fargate runs containers without servers and has no 15-minute limit; Step Functions can wait for completion.
- B: Lambda is limited to 15 minutes.
- C: Not serverless and wasteful.
- D: Not a compute service for batch containers.

### Q14 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.8 · Difficulty: Medium · Type: MC
- Correct D: OpenSearch supports near-real-time search and dashboards on log data.
- A: Query latency and no dashboards by default.
- B: Nightly batch.
- C: Not suited to search.

### Q15 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.3.6 · Difficulty: Medium · Type: MC
- Correct B: PITR provides continuous backups with restore to any second within the retention window (up to 35 days).
- A: Streams capture a 24-hour change log, not a restorable backup.
- C: A cache.
- D: Replication that would also replicate the delete.

### Q16 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.3 · Difficulty: Hard · Type: MC
- Correct C: Schema Registry stores versioned schemas and enforces compatibility modes for streaming producers and consumers.
- A: Crawlers infer table schemas, not enforce stream compatibility.
- B: Finds sensitive data.
- D: Tracks resource configuration.

### Q17 — C, D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.7 · Difficulty: Hard · Type: MR
- Correct C and D: Cross-account sharing grants from the owner to the account, then the recipient creates resource links and grants onward.
- A: Insecure and unnecessary.
- B: Not governed.
- E: Duplicates data and bypasses governance.

### Q18 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.5 · Difficulty: Medium · Type: MC
- Correct D: Federated queries run SQL against external sources through connectors.
- A: Crawlers catalog metadata, they do not join.
- B: Redshift feature.
- C: S3 Select reads within S3 objects only.

### Q19 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.1 · Difficulty: Medium · Type: MC
- Correct A: Row-level security filters data per user or group.
- B: Does not scale.
- C: Exposes all data.
- D: Controls columns, not rows.

### Q20 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.4 · Difficulty: Medium · Type: MC
- Correct B: Flex uses spare capacity at a lower price for non-time-critical jobs.
- A: Raises cost.
- C: Not a Glue job feature.
- D: Changes engine capabilities, not price class.

### Q21 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.7 · Difficulty: Hard · Type: MC
- Correct C: Compaction rewrites small files into larger ones to reduce metadata and I/O.
- A: Slower and loses table features.
- B: Destructive.
- D: More partitions create more small files.

### Q22 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.4.3 · Difficulty: Medium · Type: MC
- Correct A: CloudTrail Lake stores events and supports SQL queries, including organization-wide.
- B: Requires infrastructure.
- C: Visualizes metrics.
- D: Finds sensitive data in S3.
