# B. Skills Gap Analysis

> Maps your existing data engineering knowledge to AWS-specific concepts you need to learn for DEA-C01.

## Gap Analysis Table

| What You Already Know | AWS Service/Concept to Learn | Why It Matters for DEA-C01 | Difficulty | Priority | Best Resource | Suggested Exercise |
|---|---|---|---|---|---|---|
| ETL pipelines, Spark, data transformation | **AWS Glue** (ETL jobs, crawlers, Data Catalog, bookmarks, DataBrew, Glue Studio) | Domain 1 — 34% of exam. Glue is THE central ETL service. | Medium | **HIGH** | [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) | Create a Glue crawler on S3, run a Glue ETL job |
| Kafka, streaming, event processing | **Amazon Kinesis** (Data Streams, Firehose, Data Analytics) | Domain 1 — streaming ingestion is heavily tested | Medium | **HIGH** | [Kinesis Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) | Compare Streams vs Firehose decision matrix |
| Kafka specifically | **Amazon MSK** (Managed Streaming for Apache Kafka) | Domain 1 — Kafka-on-AWS, MSK Connect, MSK Serverless | Low | **MEDIUM** | [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) | Map your Kafka knowledge to MSK terminology |
| Data warehousing, SQL analytics, columnar storage | **Amazon Redshift** (Spectrum, COPY, distribution/sort keys, RA3, Serverless) | Domain 2 — 26% of exam. Redshift is the primary DW. | Medium | **HIGH** | [Redshift Getting Started](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) | Practice COPY command syntax, understand dist styles |
| SQL querying, ad-hoc analysis | **Amazon Athena** (serverless SQL on S3, partition projection, CTAS, workgroups) | Domain 1+2 — common "query S3 data" answer | Low | **HIGH** | [Athena User Guide](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) | Write a CTAS query with partitioning |
| Object storage concepts (you know S3 basics) | **S3 Deep Dive** (storage classes, lifecycle, versioning, S3 Select, access points, event notifications) | Domain 2 — S3 is foundational to everything | Low | **HIGH** | [S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) | Design a lifecycle policy for hot/warm/cold data |
| Data lake concepts, access control | **AWS Lake Formation** (permissions, data filters, governed tables, blueprints) | Domain 4 — 18% of exam. Central to data governance. | Medium | **HIGH** | [Lake Formation Developer Guide](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) | Set up column-level permissions on a table |
| RBAC, authentication, authorization | **AWS IAM** (policies, roles, trust policies, cross-account, service roles, SCPs) | Domain 4 — appears in EVERY domain. Foundational. | High | **HIGH** | [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) | Write a policy that grants Glue access to S3 |
| Encryption at rest/in transit | **AWS KMS** (CMKs, envelope encryption, key policies, grants, S3 SSE options) | Domain 4 — encryption questions are guaranteed | Medium | **HIGH** | [KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) | Compare SSE-S3 vs SSE-KMS vs SSE-C |
| Workflow orchestration (Airflow, etc.) | **AWS Step Functions** (state machines, error handling, Map state, parallel execution) | Domain 3 — orchestration is a key topic | Low | **HIGH** | [Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) | Design a state machine for an ETL pipeline |
| Spark, distributed processing | **Amazon EMR** (Spark on EMR, EMRFS, EMR Serverless, EMR on EKS) | Domain 1 — "when Glue vs EMR" is a classic question | Medium | **MEDIUM** | [EMR Management Guide](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) | Compare Glue vs EMR decision criteria |
| Monitoring, logging, alerting | **Amazon CloudWatch** (metrics, logs, alarms, dashboards, Logs Insights) | Domain 3 — operational monitoring | Low | **MEDIUM** | [CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) | Set up a Glue job failure alarm |
| Audit logging | **AWS CloudTrail** (management events, data events, trails, log file integrity) | Domain 4 — audit and compliance | Low | **MEDIUM** | [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) | Understand management vs data events |
| Event-driven architecture | **Amazon EventBridge** (rules, event buses, scheduling, targets) | Domain 3 — event-driven pipeline triggers | Low | **MEDIUM** | [EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) | Create a rule that triggers Lambda on S3 upload |
| Serverless functions (you know Lambda basics) | **Lambda Deep Dive** (event sources, concurrency, DLQ, layers, destinations) | Domain 1+3 — Lambda as glue between services | Low | **MEDIUM** | [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) | Map Lambda event source integrations |
| Data modeling, schema design | **Glue Data Catalog** (databases, tables, schema versioning, schema registry) | Domain 2 — central metadata store | Low | **MEDIUM** | [Glue Data Catalog docs](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) | Understand how Athena/Redshift Spectrum use the catalog |
| Data quality, validation | **AWS Glue Data Quality** (DQDL rules, recommendations, CloudWatch integration) | Domain 3+4 — data quality is a newer exam topic | Medium | **MEDIUM** | [Glue Data Quality docs](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) | Write 3 DQDL rules for a sample dataset |
| Networking basics | **VPC for Data Services** (VPC endpoints, PrivateLink, security groups, NAT gateway) | Domain 4 — secure data access patterns | Medium | **LOW** | [VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) | Understand when Glue needs a VPC connection |
| BI, dashboarding | **Amazon QuickSight** (SPICE, datasets, dashboards, row-level security) | Domain 2 — 1-2 questions max | Low | **LOW** | [QuickSight User Guide](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) | Know SPICE and when to use QuickSight |
| Relational databases | **Amazon RDS / Aurora** (read replicas, Multi-AZ, Aurora Serverless, DMS) | Domain 2 — source system for data pipelines | Low | **LOW** | [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) | Understand DMS for migration scenarios |

## Your Advantage Areas

These are topics where your existing knowledge gives you a head start:

- **Data formats** (Parquet, ORC, Avro) — you just need to learn AWS-specific optimizations
- **Partitioning strategies** — same concepts, just applied to S3/Hive-style partitions
- **Batch vs streaming** — you understand the tradeoffs, just need to map to Kinesis/MSK/Glue Streaming
- **Data modeling** — star schema, denormalization, SCD — same in Redshift
- **SQL** — Athena uses Presto/Trino SQL, Redshift uses PostgreSQL-compatible SQL
- **Python** — Glue ETL uses PySpark, Lambda uses Python
- **Orchestration** — Step Functions is simpler than Airflow conceptually

## Your Risk Areas

These need the most attention:

1. **IAM policy syntax and evaluation logic** — AWS-specific, no equivalent elsewhere
2. **Lake Formation permission model** — unique to AWS, replaces IAM for data lake
3. **Kinesis Streams vs Firehose vs Data Analytics** — the decision tree is exam-critical
4. **Glue job bookmarks, crawlers, classifiers** — AWS-specific ETL concepts
5. **Redshift distribution styles and sort keys** — performance tuning is tested
6. **KMS encryption options** — SSE-S3 vs SSE-KMS vs SSE-C vs client-side
7. **Service selection questions** — "which service for this scenario?" requires pattern recognition
