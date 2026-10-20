# Domain 1 — Ingestion & Transformation (34 %) — one-pager
Task map: 1.1 ingest · 1.2 transform · 1.3 orchestrate · 1.4 programming. Details: `08-streaming`, `09-glue`, `06-formats`, `00-which-service-when`.

## Rapid decisions
- Real-time + replay + multi-consumer → KDS/MSK. Land in S3/Redshift/OpenSearch with no code → Firehose. Windows/joins → Flink.
- Schedule → EventBridge Scheduler / MWAA / Glue trigger. S3 object created → S3 Event Notification (Lambda/SQS/SNS/EventBridge). Lambda reads Kinesis via event source mapping (batch size, batching window, parallelization factor, bisect-on-error, DLQ/on-failure destination) (1.1.7).
- IP allowlist for data sources (1.1.8): NAT Gateway/Elastic IP gives static egress for Glue/Lambda in VPC; security group rules; source firewall allows those IPs.
- Throttling (1.1.9): exponential backoff + jitter, batching, DynamoDB on-demand/auto scaling, RDS Proxy ~, SQS as buffer, Kinesis shards/EFO.
- Replayability (1.1.11): immutable raw layer, idempotent writes, retention, bookmarks reset, Iceberg time travel.
- Transform engine: Glue (default) · EMR (control/scale/spot) · Lambda (<15 min ✓) · Athena/Redshift (SQL) · Flink (stream) · DataBrew (no code) — 1.2.5.
- Format conversion CSV/JSON → **Parquet + Snappy**, partition by date (1.2.6) — Glue job, Athena CTAS, Firehose conversion, EMR.
- Connect to sources via JDBC/ODBC (Glue connections; Redshift/Athena drivers) (1.2.2). Multiple sources → Glue joins / Athena federated query / Redshift federated / zero-ETL (1.2.3).
- Cost (1.2.4): Spot/Flex on EMR/Glue, auto scaling, columnar+partition pruning, right-size, serverless for spiky, batch not streaming where latency allows, S3 tiering, avoid small files.
- Data APIs (1.2.8/1.1.4): API Gateway + Lambda (+Athena/DynamoDB), AppSync out of scope ✓; consume APIs with Lambda/Glue/AppFlow, respect rate limits.
- 3 Vs (1.2.9): volume → partition/scale-out; velocity → streaming; variety → schema-on-read, Glue DynamicFrame, Iceberg schema evolution.
- **LLMs in pipelines (1.2.10, new v1.1)**: Bedrock invoked from Lambda/Step Functions/Glue for enrichment, classification, summarisation, PII redaction, embeddings → vector store; batch inference for bulk; cost/latency controls (batching, caching), guardrails ~. Know *when*, not API syntax.
- Orchestration (1.3): Step Functions (Standard ≤1 y / Express ≤5 min ✓; Retry/Catch, Map/Distributed Map ≤10k children ✓, `.sync` integrations for Glue/EMR/Athena/Batch) vs MWAA vs Glue workflows vs EventBridge. Resiliency: retries with backoff, DLQ, idempotency, multi-AZ managed services, checkpoints, alerts SNS/SQS (1.3.4).
- Programming (1.4): Lambda concurrency — reserved (guarantee + cap), provisioned (no cold start), account 1,000 ✓; batch size & timeout 15 min ✓; memory↔CPU (1,769 MB = 1 vCPU ✓); mount **EFS** for shared/large state (1.4.7), /tmp up to 10 GB ✓. SAM = CFN extension for serverless (`sam build/deploy`, `AWS::Serverless::Function`) ; CDK = code → CFN; CFN StackSets/drift ~; CI/CD: CodePipeline + CodeBuild + CodeDeploy (CodeCommit removed from scope ✓), tests, git, blue/green, versioned Glue scripts in S3.
- Distributed computing (1.4.10): partition data, shuffle cost, skew, map-reduce; data structures (1.4.11): trees/graphs (Neptune graph traversal).

## Trap list
- Firehose ≠ replay; KDS ≠ auto-delivery to S3. “Near real-time” usually Firehose.
- Kinesis consumers > 2 competing on shared throughput → EFO.
- Lambda cannot run >15 min → Glue/EMR/Step Functions + Batch.
- Crawling huge S3 every run is slow → partition projection / targeted crawl.
- MWAA is always-on cost; Step Functions pay per transition.
- “Least operational overhead” never picks EMR on EC2 or self-managed Kafka.
