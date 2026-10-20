# Mock Exam 2 — Part 3 Answers & Explanations (Q45–65)

### Q45 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.4 · Difficulty: Medium · Type: MC
- Correct D: A Python shell job has no 15-minute limit and suits light API-to-S3 work serverlessly.
- A: Lambda times out at 15 minutes.
- B: Servers to manage.
- C: Overkill.

### Q46 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.2 · Difficulty: Hard · Type: MC
- Correct A: Partitioned reads open multiple parallel connections.
- B: Idle workers if the read is serial.
- C: Less parallelism.
- D: Would stop the read.

### Q47 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.4.6 · Difficulty: Medium · Type: MC
- Correct B: Knowledge Bases manages ingestion, chunking, embedding, storage, and retrieval.
- A: A data warehouse, not a managed RAG pipeline.
- C: Visual data prep.
- D: Streaming delivery.

### Q48 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.6 · Difficulty: Medium · Type: MC
- Correct C: Log archiving to S3 preserves logs after termination.
- A: Does not preserve logs.
- B: Scales nodes.
- D: Unrelated.

### Q49 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.5 · Difficulty: Hard · Type: MC
- Correct B: Endpoint policies restrict which resources can be accessed through the endpoint.
- A: Gateway endpoints do not use security groups.
- C: Unrelated.
- D: DNS does not control authorization.

### Q50 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.10 · Difficulty: Hard · Type: MC
- Correct C: Batch inference processes large volumes asynchronously at lower cost than on-demand calls.
- A: Risks throttling and higher per-request cost.
- B: Training is out of scope and unnecessary.
- D: An image analysis service.

### Q51 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.3 · Difficulty: Medium · Type: MC
- Correct D: pgvector adds vector similarity search to PostgreSQL alongside relational joins.
- A: A separate store without SQL joins.
- B: Filters within an object.
- C: Not part of the application database.

### Q52 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.2 · Difficulty: Medium · Type: MC
- Correct A: DAG parse errors are reported in the DAG processing logs, and path misconfiguration prevents discovery.
- B: Unlikely first check.
- C: Unrelated.
- D: Unrelated.

### Q53 — B

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.1.2 · Difficulty: Medium · Type: MC
- Correct B: Transfer Family provides managed SFTP, FTPS, and FTP endpoints backed by S3.
- A: Agent-based transfer between storage systems.
- C: Offline appliance.
- D: SaaS integration.

### Q54 — C, E

- Domain: D2 (Data Store Management) · Task/skill: 2.3.6 · Difficulty: Medium · Type: MR
- Correct C and E: Versioning preserves prior versions; MFA delete or Object Lock restricts deletion.
- A: Performance.
- B: Billing.
- D: Logging does not prevent deletion.

### Q55 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.4 · Difficulty: Medium · Type: MC
- Correct D: Athena for Apache Spark provides serverless interactive notebooks.
- A: Servers to manage.
- B: Cluster management.
- C: SQL editor, not PySpark.

### Q56 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.4 · Difficulty: Hard · Type: MC
- Correct A: Hybrid access mode lets selected principals and tables use Lake Formation while others continue with IAM-based access.
- B: Would break jobs.
- C: Insecure.
- D: Unrelated.

### Q57 — C

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.2.5 · Difficulty: Medium · Type: MC
- Correct C: EMR Serverless runs Spark without managing clusters and scales per job.
- A: Cluster management and idle cost.
- B: SQL service; custom libraries are limited.
- D: Not a Spark service.

### Q58 — A

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.9 · Difficulty: Medium · Type: MC
- Correct A: A pipeline with tests and IaC provides repeatable CI/CD.
- B: Manual and unversioned.
- C: Manual.
- D: No testing or rollbacks.

### Q59 — D

- Domain: D1 (Data Ingestion and Transformation) · Task/skill: 1.4.6 · Difficulty: Medium · Type: MC
- Correct D: SAM simplifies serverless resource definitions and offers local build, invoke, and deploy.
- A: No higher-level model.
- B: Not repeatable.
- C: Unrelated.

### Q60 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.3.6 · Difficulty: Medium · Type: MC
- Correct C: CRR replicates objects asynchronously to a bucket in another Region and requires versioning.
- A: Faster uploads, not replication.
- B: Query feature.
- D: Network connectivity.

### Q61 — A, C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.2 · Difficulty: Medium · Type: MR
- Correct A and C: Express One Zone uses directory buckets in one AZ for very low latency.
- B: Data is stored in one AZ.
- D: It targets hot, latency-sensitive data.
- E: No restore step.

### Q62 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.4 · Difficulty: Medium · Type: MC
- Correct B: Grouping reduces per-file overhead and task counts.
- A: Reduces resources.
- C: Does not address small files.
- D: Masks the issue.

### Q63 — A, C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.4.4 · Difficulty: Medium · Type: MR
- Correct A and C: Stratified and random sampling keep samples representative and reproducible.
- B: Biased by file order.
- D: Biased.
- E: Skips the requirement.

### Q64 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.2 · Difficulty: Medium · Type: MC
- Correct D: Security configurations apply encryption settings to job outputs, logs, and bookmarks.
- A: Query feature.
- B: Discovers schema.
- C: Controls access, not encryption of job artifacts.

### Q65 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.3 · Difficulty: Medium · Type: MC
- Correct C: Account-level Block Public Access overrides bucket and object ACLs and policies that would grant public access.
- A: Not enforceable.
- B: Tags do not restrict access.
- D: Logging is detective at best.
