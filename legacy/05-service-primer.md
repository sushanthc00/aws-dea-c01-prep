# E. Service-by-Service AWS Data Engineering Primer

> Concise but useful primer on every AWS service relevant to DEA-C01.  
> For each: what it is, when to use it, when NOT to, exam traps, and familiar mappings.

---

## 1. Amazon S3 (Simple Storage Service)

**What it is**: Object storage service. The foundation of almost every AWS data architecture. Think of it as an infinitely scalable filesystem with an HTTP API.

**Familiar mapping**: Like HDFS but serverless, or like Azure Blob Storage / GCS.

**When to use it**:
- Data lake storage layer (raw, processed, curated zones)
- Landing zone for ingested data
- Staging area for Redshift COPY
- Athena query target
- Archive storage

**When NOT to use it**:
- Low-latency key-value lookups (use DynamoDB)
- Transactional workloads (use RDS/Aurora)
- Block storage for EC2 (use EBS)

**Key concepts for the exam**:
| Concept | What to Know |
|---|---|
| Storage classes | Standard, Standard-IA, One Zone-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval, Glacier Deep Archive, Intelligent-Tiering |
| Lifecycle policies | Automate transitions between storage classes and expiration |
| Versioning | Keep multiple versions of objects; required for cross-region replication |
| S3 Select | Push-down filtering — query inside objects without downloading them |
| Event notifications | Trigger Lambda/SQS/SNS/EventBridge on object creation/deletion |
| Access points | Simplified access management for shared datasets |
| S3 Transfer Acceleration | Faster uploads using CloudFront edge locations |
| Requester Pays | Requester pays for data transfer (useful for shared datasets) |

**Exam traps**:
- S3 Standard-IA has a minimum storage duration of 30 days and minimum object size of 128 KB
- Glacier Flexible Retrieval takes 1-5 minutes (expedited), 3-5 hours (standard), or 5-12 hours (bulk)
- Glacier Deep Archive takes 12 hours (standard) or 48 hours (bulk)
- S3 Intelligent-Tiering has no retrieval fees but has a small monitoring fee
- S3 is eventually consistent for overwrite PUTs and DELETEs (actually, S3 is now strongly consistent as of Dec 2020 — exam may still reference this)

---

## 2. AWS Glue

**What it is**: Fully managed ETL service. Includes a Data Catalog (metadata store), crawlers (schema discovery), ETL jobs (PySpark/Scala), and more. It's the Swiss Army knife of AWS data engineering.

**Familiar mapping**: Like a managed Apache Spark + Hive Metastore + schema registry combined.

**When to use it**:
- ETL/ELT pipelines (batch and streaming)
- Schema discovery and cataloging
- Data quality checks
- Data preparation (DataBrew)
- Central metadata store for Athena, Redshift Spectrum, EMR

**When NOT to use it**:
- Complex, long-running Spark jobs needing fine-grained cluster control (use EMR)
- Real-time stream processing with sub-second latency (use Kinesis Data Analytics/Flink)
- Simple file transformations (Lambda might be simpler)

**Key components**:

| Component | What It Does | Exam Relevance |
|---|---|---|
| **Data Catalog** | Central metadata repository (databases, tables, schemas) | HIGH — used by Athena, Spectrum, EMR |
| **Crawlers** | Auto-discover schemas from S3, JDBC, DynamoDB | HIGH — know when to use vs manual table definition |
| **ETL Jobs** | PySpark or Scala scripts for transformation | HIGH — core of Domain 1 |
| **Job Bookmarks** | Track processed data for incremental loads | HIGH — classic exam question |
| **Glue Studio** | Visual ETL job authoring | MEDIUM |
| **DataBrew** | No-code data preparation and profiling | MEDIUM |
| **Data Quality** | DQDL rules for validation | MEDIUM — newer topic |
| **Schema Registry** | Schema versioning for streaming (Avro, JSON) | MEDIUM |
| **Glue Streaming ETL** | Micro-batch processing from Kinesis/Kafka | MEDIUM |
| **Classifiers** | Custom schema detection for crawlers | LOW |

**Exam traps**:
- Glue ETL jobs run on Apache Spark — they have cold start time (not instant)
- Job bookmarks only work with S3 and JDBC sources, and only with certain formats
- Glue crawlers can be slow and may not always infer schemas correctly — sometimes manual table definition is better
- Glue Data Catalog is the default Hive metastore for Athena and can be used by EMR
- Glue Streaming ETL uses micro-batching (not true real-time)
- DPU (Data Processing Unit) = unit of compute in Glue. More DPUs = faster but more expensive

---

## 3. Amazon Redshift

**What it is**: Fully managed, petabyte-scale cloud data warehouse. Columnar storage, MPP (massively parallel processing) architecture.

**Familiar mapping**: Like Snowflake, BigQuery, or Teradata but AWS-native.

**When to use it**:
- Complex analytical queries on structured/semi-structured data
- BI reporting and dashboarding backend
- Data warehouse workloads with predictable query patterns
- When you need joins across large tables

**When NOT to use it**:
- Ad-hoc queries on raw S3 data (use Athena — no infrastructure to manage)
- OLTP workloads (use RDS/Aurora)
- Unstructured data processing (use EMR/Glue)

**Key concepts**:

| Concept | What to Know |
|---|---|
| **Architecture** | Leader node (query planning) + Compute nodes (execution) |
| **Node types** | RA3 (managed storage, recommended), DC2 (local SSD, legacy), DS2 (deprecated) |
| **Redshift Serverless** | No cluster management, pay per query — good for variable workloads |
| **Distribution styles** | KEY (hash on column), EVEN (round-robin), ALL (full copy on each node), AUTO (Redshift decides) |
| **Sort keys** | Compound (ordered columns) vs Interleaved (equal weight to all columns) |
| **COPY command** | Bulk load from S3, DynamoDB, EMR — fastest way to load data |
| **Redshift Spectrum** | Query S3 data directly using external tables (uses Glue Data Catalog) |
| **Materialized views** | Pre-computed query results, auto-refresh |
| **Concurrency scaling** | Auto-add clusters for burst read queries |
| **WLM** | Workload Management — queue and prioritize queries |
| **Federated query** | Query RDS/Aurora from Redshift |

**Exam traps**:
- COPY is always preferred over INSERT for bulk loading (exam loves this)
- Redshift Spectrum vs Athena: Spectrum is for Redshift users who want to extend to S3; Athena is standalone serverless SQL
- Distribution style KEY should be used on join columns for co-located joins
- ALL distribution is for small dimension tables (< few million rows)
- Redshift does NOT support real-time streaming ingestion natively — use Kinesis Firehose to deliver to Redshift
- UNLOAD exports data from Redshift to S3

---

## 4. Amazon Athena

**What it is**: Serverless, interactive SQL query service. Query data directly in S3 using standard SQL (Presto/Trino engine).

**Familiar mapping**: Like Presto/Trino or BigQuery's serverless model. Pay per query, no infrastructure.

**When to use it**:
- Ad-hoc queries on S3 data lake
- Quick exploration of new datasets
- When you don't want to manage any infrastructure
- Cost-effective for infrequent queries

**When NOT to use it**:
- High-concurrency BI workloads (use Redshift)
- Complex multi-table joins on large datasets (Redshift is faster)
- Real-time queries (Athena has query startup latency)

**Key concepts**:

| Concept | What to Know |
|---|---|
| **Partition projection** | Define partition patterns in table properties — avoids partition metadata lookups in Glue Catalog |
| **CTAS** | CREATE TABLE AS SELECT — transform and store query results as new table |
| **INSERT INTO** | Append query results to existing table |
| **Workgroups** | Isolate queries, set data scan limits, track costs per team |
| **Federated query** | Query non-S3 sources (RDS, DynamoDB, etc.) via Lambda connectors |
| **Athena for Apache Spark** | Run Spark notebooks in Athena (newer feature) |

**Exam traps**:
- Athena charges per TB of data scanned — use columnar formats (Parquet/ORC) and partitioning to reduce cost
- Partition projection is faster than crawlers for well-structured partition schemes
- Athena uses the Glue Data Catalog as its metastore
- Athena is NOT suitable for ETL — it's for querying. Use Glue for transformation.
- CTAS can be used to convert data formats (e.g., JSON → Parquet)

---

## 5. AWS Lake Formation

**What it is**: Service that simplifies building, securing, and managing data lakes. Sits on top of S3 + Glue Data Catalog and adds fine-grained access control.

**Familiar mapping**: Like Apache Ranger or Databricks Unity Catalog for access control on a data lake.

**When to use it**:
- Centralized data lake security and governance
- Column-level, row-level, or cell-level access control
- Cross-account data sharing
- When IAM policies for S3 become too complex

**When NOT to use it**:
- Simple S3 access control (bucket policies may suffice)
- Non-data-lake workloads

**Key concepts**:

| Concept | What to Know |
|---|---|
| **Permissions model** | Grant/Revoke on databases, tables, columns — replaces IAM for data access |
| **Data filters** | Row-level and cell-level security |
| **LF-TBAC** | Tag-based access control — assign tags to resources and principals |
| **Blueprints** | Pre-built workflows to ingest data into the lake |
| **Governed tables** | ACID transactions on S3 (built on Apache Iceberg) |
| **Cross-account sharing** | Share data catalog resources across AWS accounts |
| **Data location registration** | Register S3 paths with Lake Formation |

**Exam traps**:
- Lake Formation permissions OVERRIDE IAM S3 permissions for registered locations — this is a common confusion point
- You must register S3 locations with Lake Formation before it can manage access
- Lake Formation uses the Glue Data Catalog — they're tightly integrated
- LF-TBAC is the recommended approach for large-scale permission management
- "Hybrid mode" allows gradual migration from IAM to Lake Formation permissions

---

## 6. Amazon Kinesis

**What it is**: Family of services for real-time streaming data. Three main components with very different use cases.

**Familiar mapping**: Kinesis Data Streams ≈ Apache Kafka. Kinesis Firehose ≈ Kafka Connect + S3 sink. Kinesis Data Analytics ≈ Apache Flink.

### Kinesis Data Streams
- **What**: Real-time data streaming with shards (partitions)
- **Use when**: You need real-time processing with custom consumers, ordering guarantees, replay capability
- **Retention**: 24 hours default, up to 365 days
- **Consumers**: KCL applications, Lambda, Kinesis Data Analytics
- **Scaling**: Manual shard splitting/merging or on-demand mode
- **Enhanced fan-out**: Dedicated throughput per consumer (2 MB/s per shard per consumer)

### Kinesis Data Firehose
- **What**: Fully managed delivery service — load streaming data into destinations
- **Use when**: You want to deliver streaming data to S3, Redshift, OpenSearch, Splunk, or HTTP endpoints with zero administration
- **Key feature**: Can transform data using Lambda before delivery
- **Buffering**: Time-based (60-900 seconds) or size-based (1-128 MB)
- **Near real-time**: NOT real-time — has buffering delay (minimum ~60 seconds)
- **No data retention**: It's a delivery pipe, not a storage system

### Kinesis Data Analytics (Apache Flink)
- **What**: Run Apache Flink applications on streaming data
- **Use when**: Complex stream processing, windowed aggregations, real-time analytics
- **Supports**: SQL and Flink (Java/Scala/Python)

**Decision tree**:
```
Need to collect and process streaming data?
├── Need custom processing with replay? → Kinesis Data Streams
├── Just need to deliver to S3/Redshift/OpenSearch? → Kinesis Data Firehose
├── Need complex real-time analytics? → Kinesis Data Analytics (Flink)
└── Already using Kafka? → Amazon MSK
```

**Exam traps**:
- Firehose is NEAR real-time (buffering), not real-time — this is a classic trap
- Kinesis Data Streams requires you to manage shard capacity (unless using on-demand)
- Firehose can deliver to S3, Redshift, OpenSearch, Splunk, HTTP — but NOT directly to DynamoDB or RDS
- Enhanced fan-out is needed when you have multiple consumers and need dedicated throughput
- Kinesis Data Streams supports ordering within a shard (by partition key)

---

## 7. Amazon MSK (Managed Streaming for Apache Kafka)

**What it is**: Fully managed Apache Kafka service. Run Kafka without managing brokers, ZooKeeper, etc.

**Familiar mapping**: It IS Kafka, just managed by AWS.

**When to use it**:
- You already have Kafka expertise/applications
- You need Kafka-specific features (exactly-once semantics, Kafka Connect ecosystem)
- Migration from on-prem Kafka

**When NOT to use it**:
- Simple streaming delivery to S3 (Firehose is simpler)
- You don't need Kafka specifically (Kinesis Data Streams is simpler)

**Key concepts**:
| Concept | What to Know |
|---|---|
| **MSK Serverless** | No broker management, auto-scaling |
| **MSK Connect** | Run Kafka Connect connectors as managed service |
| **MSK Provisioned** | You choose broker type and count |
| **Schema Registry** | Can use Glue Schema Registry with MSK |

**Exam traps**:
- MSK vs Kinesis Data Streams: MSK if you need Kafka compatibility; Kinesis if you want AWS-native simplicity
- MSK Connect can replace self-managed Kafka Connect clusters
- MSK Serverless removes capacity planning but has some limitations vs provisioned

---

## 8. Amazon EMR (Elastic MapReduce)

**What it is**: Managed cluster platform for big data frameworks — Spark, Hive, Presto, HBase, Flink, etc.

**Familiar mapping**: Like Databricks or Cloudera but on AWS. You get a managed Spark/Hadoop cluster.

**When to use it**:
- Complex Spark jobs needing fine-grained cluster control
- Multi-framework workloads (Spark + Hive + Presto)
- Large-scale ML training on Spark
- When Glue's managed environment is too restrictive

**When NOT to use it**:
- Simple ETL (Glue is easier and serverless)
- Ad-hoc SQL queries (Athena is simpler)
- You don't want to manage clusters (use Glue or EMR Serverless)

**Glue vs EMR decision**:
| Factor | Choose Glue | Choose EMR |
|---|---|---|
| Operational overhead | Want zero management | OK managing clusters |
| Job complexity | Standard ETL | Complex multi-step Spark |
| Cost model | Pay per DPU-hour | Pay per EC2 instance-hour |
| Customization | Limited | Full control (libraries, configs) |
| Frameworks | Spark only | Spark, Hive, Presto, Flink, HBase |
| Startup time | Minutes (cold start) | Minutes (cluster launch) |

**Key variants**:
- **EMR on EC2**: Traditional — you manage the cluster
- **EMR on EKS**: Run Spark on your existing EKS cluster
- **EMR Serverless**: No cluster management, auto-scaling (newer)
- **EMRFS**: S3 as the storage layer for EMR (consistent view)

**Exam traps**:
- EMR Serverless is the answer when they say "minimize operational overhead" but need EMR capabilities
- EMRFS provides consistent view of S3 for EMR
- EMR can use Glue Data Catalog as its Hive metastore
- Spot instances on EMR task nodes = cost optimization (but not on master/core nodes for stability)

---

## 9. AWS Lambda

**What it is**: Serverless compute — run code without provisioning servers. Event-driven, pay per invocation.

**Familiar mapping**: Like Azure Functions or Google Cloud Functions.

**When to use it (in data engineering)**:
- Lightweight data transformations (< 15 min, < 10 GB memory)
- Event-driven triggers (S3 upload → process → write)
- Kinesis Firehose data transformation
- Glue job orchestration triggers
- API-based data ingestion

**When NOT to use it**:
- Long-running ETL jobs (15-minute timeout)
- Large data processing (10 GB memory limit)
- Complex Spark workloads (use Glue/EMR)

**Key concepts for exam**:
| Concept | What to Know |
|---|---|
| **Event sources** | S3, Kinesis, SQS, DynamoDB Streams, API Gateway, EventBridge |
| **Concurrency** | Default 1000 concurrent executions per region |
| **Reserved concurrency** | Guarantee capacity for critical functions |
| **DLQ** | Dead Letter Queue — capture failed invocations |
| **Destinations** | Route success/failure to SQS, SNS, Lambda, EventBridge |
| **Layers** | Share code/libraries across functions |
| **VPC access** | Lambda can access VPC resources (but adds cold start latency) |

**Exam traps**:
- Lambda has a 15-minute maximum timeout — not suitable for long ETL
- Lambda in VPC has additional cold start time
- Lambda + Kinesis: Lambda polls the stream (not push-based)
- Lambda + S3: S3 event notification triggers Lambda (push-based)

---

## 10. AWS IAM (Identity and Access Management)

**What it is**: Controls who can do what in AWS. Policies, roles, users, groups.

**Familiar mapping**: Like LDAP/AD + RBAC but for cloud resources. Every AWS API call is authorized through IAM.

**Key concepts**:

| Concept | What to Know |
|---|---|
| **Identity-based policies** | Attached to users/groups/roles — "what can this identity do?" |
| **Resource-based policies** | Attached to resources (S3 bucket, KMS key) — "who can access this resource?" |
| **IAM roles** | Temporary credentials for services/users — preferred over long-term keys |
| **Trust policies** | Define who can assume a role |
| **Service-linked roles** | Pre-defined roles for AWS services |
| **Cross-account access** | Use roles + trust policies to share resources across accounts |
| **Policy evaluation** | Explicit deny > explicit allow > implicit deny |
| **SCPs** | Service Control Policies in AWS Organizations — guardrails |
| **Permission boundaries** | Maximum permissions an identity can have |

**Exam traps**:
- Explicit DENY always wins — even if there's an ALLOW elsewhere
- S3 bucket policies are resource-based policies
- Glue jobs need an IAM role with permissions to access S3, Data Catalog, etc.
- Cross-account access: Account A creates a role, Account B assumes it
- Service-linked roles cannot be modified — they're managed by AWS

---

## 11. AWS KMS (Key Management Service)

**What it is**: Managed encryption key service. Create, manage, and use encryption keys.

**Familiar mapping**: Like HashiCorp Vault for key management, but AWS-native.

**S3 encryption options** (exam favorite):

| Option | Key Management | Use When |
|---|---|---|
| **SSE-S3** | AWS manages everything | Default, simplest option |
| **SSE-KMS** | You control the KMS key | Need audit trail (CloudTrail logs key usage), key rotation control |
| **SSE-C** | You provide the key with each request | Regulatory requirement to manage your own keys |
| **Client-side** | You encrypt before upload | Need end-to-end encryption |

**Key concepts**:
- **Envelope encryption**: Data key encrypts data, KMS key encrypts data key
- **Key policies**: Resource-based policies on KMS keys
- **Grants**: Temporary, fine-grained permissions on keys
- **Automatic key rotation**: Annual rotation for KMS keys (customer-managed)

**Exam traps**:
- SSE-KMS has a request rate limit (can throttle high-throughput workloads)
- SSE-S3 uses AES-256 and is now the default for new S3 buckets
- CloudTrail logs KMS API calls — useful for auditing who decrypted what
- Cross-account access to KMS keys requires both key policy AND IAM policy

---

## 12. Amazon CloudWatch

**What it is**: Monitoring and observability service. Metrics, logs, alarms, dashboards.

**Familiar mapping**: Like Datadog, Grafana + Prometheus, or ELK stack for monitoring.

**Key concepts for data engineering**:
| Concept | What to Know |
|---|---|
| **Metrics** | Numerical data points (CPU, memory, custom metrics) |
| **Logs** | Log groups and log streams from services |
| **Alarms** | Trigger actions based on metric thresholds |
| **Dashboards** | Visual monitoring |
| **Logs Insights** | SQL-like query language for log analysis |
| **Contributor Insights** | Identify top contributors to metrics |
| **Composite alarms** | Combine multiple alarms |

**Data engineering monitoring**:
- Glue job metrics: duration, DPU usage, bytes read/written
- Kinesis metrics: IncomingRecords, ReadProvisionedThroughputExceeded
- Redshift metrics: query performance, disk usage, connections
- Lambda metrics: invocations, errors, duration, throttles

---

## 13. AWS CloudTrail

**What it is**: Audit logging service. Records every API call made in your AWS account.

**Familiar mapping**: Like an audit log for all AWS operations.

**Key concepts**:
| Concept | What to Know |
|---|---|
| **Management events** | Control plane operations (CreateBucket, RunJobFlow) — logged by default |
| **Data events** | Data plane operations (GetObject, PutObject, Lambda invocations) — NOT logged by default, must enable |
| **Trails** | Configuration for where to deliver logs (S3 bucket) |
| **Log file integrity** | Validate that log files haven't been tampered with |
| **Organization trails** | Single trail for all accounts in AWS Organizations |

**Exam traps**:
- Data events are NOT enabled by default — you must explicitly configure them
- CloudTrail logs are delivered to S3 — you can query them with Athena
- CloudTrail + Athena is a common pattern for security analysis
- Management events are free (90-day history); data events cost extra

---

## 14. AWS Step Functions

**What it is**: Serverless orchestration service. Visual workflow for coordinating AWS services.

**Familiar mapping**: Like Apache Airflow but serverless and visual. State machine-based.

**When to use it**:
- Orchestrate multi-step ETL pipelines
- Coordinate Glue jobs, Lambda functions, EMR steps
- Error handling and retry logic
- Parallel processing workflows

**Key concepts**:
| Concept | What to Know |
|---|---|
| **Standard workflows** | Long-running (up to 1 year), exactly-once execution, higher cost |
| **Express workflows** | Short-duration (up to 5 min), at-least-once, lower cost, high volume |
| **State types** | Task, Choice, Parallel, Map, Wait, Pass, Succeed, Fail |
| **Error handling** | Retry and Catch blocks on states |
| **Map state** | Process items in an array (like a for-each loop) |
| **Service integrations** | Direct integration with 200+ AWS services |

**Exam traps**:
- Standard vs Express: Standard for ETL orchestration; Express for high-volume, short-duration
- Step Functions can directly invoke Glue jobs, Lambda, EMR, Athena queries
- Step Functions vs EventBridge: Step Functions for sequential workflows; EventBridge for event-driven routing
- Map state with distributed mode can process millions of items in parallel

---

## 15. Amazon EventBridge

**What it is**: Serverless event bus. Route events between AWS services, SaaS apps, and custom applications.

**Familiar mapping**: Like a message broker / event router. Think of it as a smart event dispatcher.

**When to use it**:
- Schedule-based triggers (cron jobs)
- Event-driven pipeline triggers (S3 event → start Glue job)
- Cross-service event routing
- Decoupled architectures

**Key concepts**:
| Concept | What to Know |
|---|---|
| **Event bus** | Channel for events (default, custom, partner) |
| **Rules** | Match events and route to targets |
| **Targets** | Lambda, Step Functions, SQS, SNS, Glue, etc. |
| **Scheduling** | Cron and rate-based schedules |
| **Schema registry** | Discover and store event schemas |

---

## 16. VPC Basics for Data Services

**What it is**: Virtual Private Cloud — isolated network in AWS.

**What you need to know for the exam** (not deep networking):

| Concept | Why It Matters |
|---|---|
| **VPC endpoints** | Access S3, DynamoDB, Glue without going through the internet (Gateway endpoints for S3/DynamoDB, Interface endpoints for others) |
| **PrivateLink** | Access AWS services privately |
| **Security groups** | Stateful firewall for instances/services |
| **NAT Gateway** | Allow private subnet resources to access the internet |
| **Glue connections** | Glue needs a VPC connection to access JDBC sources in a VPC |

**Exam traps**:
- S3 Gateway endpoint is FREE — always use it for S3 access from VPC
- Glue jobs accessing JDBC sources in a VPC need a Glue connection with VPC/subnet/security group
- Interface endpoints have a cost; Gateway endpoints (S3, DynamoDB) are free

---

## 17. Data Formats, Partitioning, and Compression

### Data Formats

| Format | Type | Best For | Exam Notes |
|---|---|---|---|
| **Parquet** | Columnar, binary | Analytics queries, Athena, Redshift Spectrum | Default choice for analytical workloads |
| **ORC** | Columnar, binary | Hive/EMR workloads | Similar to Parquet, more Hive-native |
| **Avro** | Row-based, binary | Streaming, schema evolution | Good for Kafka/Kinesis, schema in file |
| **JSON** | Row-based, text | Raw ingestion, APIs | Human-readable but inefficient for analytics |
| **CSV** | Row-based, text | Simple data exchange | No schema, no types — avoid for analytics |

### Compression

| Algorithm | Splittable? | Ratio | Speed | Use With |
|---|---|---|---|---|
| **Snappy** | Yes (in Parquet/ORC) | Medium | Fast | Default for Parquet in Spark/Glue |
| **GZIP** | No | High | Slow | When storage cost matters most |
| **ZSTD** | Yes (in Parquet) | High | Fast | Best balance of ratio and speed |
| **LZO** | Yes (with index) | Medium | Fast | Legacy Hadoop workloads |
| **BZIP2** | Yes | Highest | Slowest | Rarely used |

### Partitioning

- **Hive-style partitioning**: `s3://bucket/table/year=2024/month=01/day=15/`
- **Why**: Reduces data scanned by Athena/Spectrum (cost and performance)
- **Too many partitions**: Small files problem — each partition should have files > 128 MB
- **Too few partitions**: Full table scans
- **Partition projection**: Define partition scheme in Athena table properties — avoids Glue Catalog lookups

### Small Files Problem
- Many small files = slow queries (overhead per file)
- Solution: Use Glue ETL to compact small files into larger ones
- Target file size: 128 MB - 512 MB for optimal performance
- S3 Inventory can help identify small files

---

## 18. Cost Optimization Patterns

| Pattern | How |
|---|---|
| Reduce Athena costs | Use Parquet/ORC, partition data, use workgroup scan limits |
| Reduce S3 costs | Lifecycle policies, Intelligent-Tiering, compress data |
| Reduce Redshift costs | Reserved instances, pause/resume, concurrency scaling limits |
| Reduce Glue costs | Right-size DPUs, use job bookmarks for incremental processing |
| Reduce Kinesis costs | Right-size shards, use on-demand mode for variable traffic |
| Reduce EMR costs | Spot instances for task nodes, auto-scaling, EMR Serverless |
| Reduce Lambda costs | Optimize memory allocation, reduce invocation count |
