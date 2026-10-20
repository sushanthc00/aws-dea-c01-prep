# Topic Set — Part 1 Answers & Explanations (Q1–24)

### Q1 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.8 · Difficulty: Medium · Type: MC
- Correct B: Outbound traffic from the private subnet leaves through the NAT gateway with a fixed Elastic IP, which the partner can allow-list.
- A: Gateway endpoints reach S3 only.
- C: Provides private access to the Glue API, not outbound internet with a fixed IP.
- D: DNS does not provide a source IP.

### Q2 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.12 · Difficulty: Medium · Type: MC
- Correct D: Deduplication needs state kept across events within a time window.
- A: Stateless logic cannot know whether an ID was seen before.
- B: Not real time.
- C: Unrelated.

### Q3 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.9 · Difficulty: Medium · Type: MC
- Correct A: A data lake on S3 with schema-on-read handles structured, semi-structured, and unstructured data.
- B: Rigid and breaks with schema changes.
- C: Poor fit for documents, images, and analytics.
- D: Loses data.

### Q4 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.4 · Difficulty: Easy · Type: MC
- Correct C: SNS fans out to multiple protocols including email and SMS.
- A: No notification.
- B: Manual.
- D: Queues do not notify people.

### Q5 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.3 · Difficulty: Hard · Type: MC
- Correct A: Parallel load splits big tables into segments loaded concurrently; more parallel subtasks use available capacity.
- B: Slows the migration.
- C: Does not speed up the full load.
- D: Order does not help throughput.

### Q6 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.5 · Difficulty: Medium · Type: MC
- Correct B: Workflows chain crawlers and jobs with conditional triggers on success.
- A: Brittle timing that breaks if the crawler runs long.
- C: Wasteful and fragile.
- D: Unrelated.

### Q7 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.1 · Difficulty: Medium · Type: MC
- Correct C: EMR on EKS runs Spark jobs as pods on existing Kubernetes capacity.
- A: Runs on Glue-managed resources, not the EKS cluster.
- B: A separate cluster, not shared.
- D: Not suitable for Spark.

### Q8 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.7 · Difficulty: Hard · Type: MC
- Correct D: S3 request rates scale per prefix (3,500 writes and 5,500 reads per second); spreading keys and reducing request count addresses throttling.
- A: More workers increase request pressure.
- B: Not a cause.
- C: Does not address the cause.

### Q9 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.8 · Difficulty: Medium · Type: MC
- Correct B: Serverless API with a key-value store gives low-latency lookups.
- A: Servers to manage.
- C: Seconds per query and cost per scan.
- D: Not designed for high-concurrency key lookups.

### Q10 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.2 · Difficulty: Medium · Type: MC
- Correct A: Retry configures attempts and exponential backoff; Catch handles the final failure.
- B: Runs branches concurrently.
- C: Passes input along.
- D: Only delays.

### Q11 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.3 · Difficulty: Hard · Type: MC
- Correct C: Standard workflows run up to a year and support callback tokens for human approval.
- A: Express workflows end after 5 minutes.
- B: Iterates over items.
- D: Branches on data.

### Q12 — B, D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.1 · Difficulty: Hard · Type: MR
- Correct B and D: Reusing connections and batching writes cut per-invocation overhead.
- A: Connection setup per record is slow.
- C: Single inserts add round trips.
- E: Lower memory also lowers CPU and can lengthen runtime.

### Q13 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.4 · Difficulty: Medium · Type: MC
- Correct D: Small fast tests in CI catch defects early.
- A: Risky.
- B: Reactive.
- C: Slow and costly.

### Q14 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.5 · Difficulty: Medium · Type: MC
- Correct A: IaC gives repeatable, reviewable deployments with parameters.
- B: Drift-prone.
- C: Divergence risk.
- D: Manual.

### Q15 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.10 · Difficulty: Medium · Type: MC
- Correct B: Broadcast joins avoid shuffling the large table.
- A: Does not remove the shuffle.
- C: Slower.
- D: Removes parallelism.

### Q16 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.10 · Difficulty: Medium · Type: MC
- Correct D: Multiple consumers can read the same stream; Firehose handles archival with no code.
- A: Extra producer complexity.
- B: Not real time.
- C: Adds unnecessary coupling.

### Q17 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.1 · Difficulty: Medium · Type: MC
- Correct B: DynamoDB can stream changes to Kinesis and Firehose delivers them to S3 without code.
- A: Expensive and misses intermediate changes.
- C: Coarse and heavy.
- D: Athena does not query DynamoDB directly this way for change capture.

### Q18 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.2 · Difficulty: Medium · Type: MC
- Correct C: DataSync schedules transfers, verifies data, and controls bandwidth.
- A: Offline appliance for one-time bulk moves.
- B: Provides SFTP endpoints for partners.
- D: Database replication.

### Q19 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.4 · Difficulty: Medium · Type: MC
- Correct A: Auto scaling matches workers to workload and cuts idle spend.
- B: Increases cost.
- C: Loses Spark.
- D: Unrelated.

### Q20 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.6 · Difficulty: Medium · Type: MC
- Correct D: Avro is row oriented, embeds its schema, and handles schema evolution well for write-heavy streaming.
- A: No schema or types.
- B: Columnar, better for analytics reads.
- C: No structure.

### Q21 — A, C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.3.1 · Difficulty: Medium · Type: MR
- Correct A and C: MWAA fits existing Airflow code and Airflow features.
- B: Step Functions suits this better.
- D: That is a Step Functions pricing model.
- E: MWAA environments have a size class and run continuously.

### Q22 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.9 · Difficulty: Medium · Type: MC
- Correct B: Offloading reads to a replica or snapshot export protects the primary.
- A: More parallel reads add load.
- C: Worsens contention.
- D: Does not help and is unsafe.

### Q23 — A, D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.6 · Difficulty: Easy · Type: MR
- Correct A and D: S3 can notify Lambda, SQS, SNS, and EventBridge.
- B: Start Glue through EventBridge or Lambda, not directly.
- C: Not a destination.
- E: Not a destination.

### Q24 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.7 · Difficulty: Medium · Type: MC
- Correct C: Ephemeral storage is configurable up to 10,240 MB.
- A: Memory does not change /tmp size.
- B: Irrelevant.
- D: Environment variables are limited to 4 KB.
