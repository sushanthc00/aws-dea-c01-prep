# Must-Know Checklist — AWS DEA-C01

> Check off each item as you become confident. Target: 90%+ checked before exam day.

## Domain 1: Data Ingestion and Transformation (34%)

### AWS Glue
- [ ] Explain Glue architecture (Data Catalog, Crawlers, ETL Jobs)
- [ ] Know when to use Glue crawlers vs manual table definitions
- [ ] Understand job bookmarks for incremental processing
- [ ] Know DynamicFrames vs DataFrames
- [ ] Understand ResolveChoice for schema conflicts
- [ ] Know Glue Streaming ETL (micro-batch from Kinesis/Kafka)
- [ ] Understand Glue DataBrew for no-code data prep
- [ ] Know Glue Data Quality (DQDL) rules
- [ ] Understand Glue Schema Registry
- [ ] Know Glue Python Shell vs Spark jobs
- [ ] Understand DPU allocation and auto-scaling

### Amazon Kinesis
- [ ] Differentiate Kinesis Data Streams vs Firehose vs Data Analytics
- [ ] Know shard capacity (1 MB/s in, 2 MB/s out)
- [ ] Understand partition keys and ordering guarantees
- [ ] Know enhanced fan-out for multiple consumers
- [ ] Understand Firehose buffering (time + size)
- [ ] Know Firehose destinations (S3, Redshift, OpenSearch, Splunk, HTTP)
- [ ] Understand Firehose Lambda transformation
- [ ] Know Firehose dynamic partitioning
- [ ] Understand Firehose format conversion (JSON → Parquet)
- [ ] Know Kinesis Data Analytics = Apache Flink

### Amazon MSK
- [ ] Know MSK vs Kinesis decision criteria
- [ ] Understand MSK Serverless vs Provisioned
- [ ] Know MSK Connect for managed Kafka connectors

### Data Formats & Optimization
- [ ] Compare Parquet vs ORC vs Avro vs JSON vs CSV
- [ ] Know compression options (Snappy, GZIP, ZSTD, LZO)
- [ ] Understand the small files problem and solutions
- [ ] Know optimal file sizes (128-512 MB)
- [ ] Understand Hive-style partitioning

### Other Ingestion
- [ ] Know AWS DMS for database migration with CDC
- [ ] Know Amazon AppFlow for SaaS ingestion
- [ ] Know AWS Transfer Family for SFTP

## Domain 2: Data Store Management (26%)

### Amazon S3
- [ ] Know all storage classes and when to use each
- [ ] Understand lifecycle policies
- [ ] Know S3 Select for push-down filtering
- [ ] Understand S3 event notifications
- [ ] Know S3 versioning and its implications
- [ ] Understand S3 access points

### Amazon Redshift
- [ ] Explain Redshift architecture (leader + compute nodes)
- [ ] Know distribution styles (KEY, EVEN, ALL, AUTO)
- [ ] Know sort keys (compound vs interleaved)
- [ ] Understand COPY command best practices
- [ ] Know UNLOAD for exporting to S3
- [ ] Understand Redshift Spectrum
- [ ] Know materialized views
- [ ] Understand concurrency scaling
- [ ] Know Redshift Serverless vs Provisioned
- [ ] Understand WLM (Workload Management)
- [ ] Know Redshift Federated Query (to RDS/Aurora)

### Amazon Athena
- [ ] Know Athena as serverless SQL on S3
- [ ] Understand partition projection
- [ ] Know CTAS for format conversion
- [ ] Understand workgroups for cost control
- [ ] Know Athena Federated Query

### Glue Data Catalog
- [ ] Understand it as the central metastore
- [ ] Know it's used by Athena, Spectrum, EMR, Lake Formation

### Other Storage
- [ ] Know DynamoDB basics (partition key, sort key, streams, TTL)
- [ ] Know RDS/Aurora basics (read replicas, Multi-AZ)
- [ ] Know QuickSight basics (SPICE, dashboards)

## Domain 3: Data Operations and Support (22%)

### Orchestration
- [ ] Know Step Functions Standard vs Express
- [ ] Understand state types (Task, Choice, Parallel, Map, Wait, Pass)
- [ ] Know retry and catch error handling
- [ ] Understand Map state for parallel processing

### Event-Driven
- [ ] Know EventBridge rules, event buses, targets
- [ ] Understand EventBridge scheduling (cron/rate)
- [ ] Know S3 event notifications → Lambda/EventBridge patterns

### Monitoring
- [ ] Know CloudWatch metrics, logs, alarms, dashboards
- [ ] Understand CloudWatch Logs Insights
- [ ] Know key metrics for Glue, Kinesis, Redshift, Lambda

### Troubleshooting
- [ ] Know common Glue job failures (OOM, connection timeout, data skew)
- [ ] Understand Kinesis throttling (ProvisionedThroughputExceeded)
- [ ] Know Redshift performance issues (VACUUM, distribution, sort keys)

### Data Quality
- [ ] Know Glue Data Quality (DQDL)
- [ ] Understand data quality integration in ETL pipelines

## Domain 4: Data Security and Governance (18%)

### IAM
- [ ] Understand identity-based vs resource-based policies
- [ ] Know policy evaluation logic (explicit deny wins)
- [ ] Understand IAM roles and trust policies
- [ ] Know cross-account access patterns
- [ ] Understand service-linked roles
- [ ] Know the principle of least privilege

### Encryption (KMS)
- [ ] Know SSE-S3 vs SSE-KMS vs SSE-C
- [ ] Understand envelope encryption
- [ ] Know KMS key policies and grants
- [ ] Understand automatic key rotation
- [ ] Know encryption in transit (TLS)

### Lake Formation
- [ ] Understand Lake Formation permission model
- [ ] Know data filters (column, row, cell-level security)
- [ ] Understand LF-TBAC (tag-based access control)
- [ ] Know cross-account data sharing
- [ ] Understand Lake Formation vs IAM for data access

### Audit & Compliance
- [ ] Know CloudTrail management events vs data events
- [ ] Understand CloudTrail log file integrity validation
- [ ] Know Amazon Macie for PII detection
- [ ] Understand AWS Config for compliance monitoring
- [ ] Know S3 Object Lock for data retention

### Networking
- [ ] Know VPC endpoints (Gateway for S3/DynamoDB, Interface for others)
- [ ] Understand Glue VPC connections for JDBC sources
- [ ] Know Redshift enhanced VPC routing

---

## Final Recommendation

Given your profile (strong DE fundamentals, some AWS exposure, 2 hrs/day for 14 days):

**Go with the 14-day plan.** You have enough time to build solid AWS knowledge without rushing. The 7-day plan is viable as a backup but leaves less room for practice exams and gap closure.

Your biggest advantages: you already understand data engineering patterns, so you just need to learn the AWS service names and decision criteria. Focus your energy on:
1. Glue (all components)
2. Kinesis (all flavors)
3. Redshift (distribution, sort keys, COPY)
4. IAM + KMS + Lake Formation
5. Service selection decision trees

If you score 75%+ on both mock exams and can check off 90% of this checklist, you're ready.
