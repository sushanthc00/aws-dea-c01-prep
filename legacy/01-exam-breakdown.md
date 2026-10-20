# A. Exam Breakdown — AWS Certified Data Engineer Associate (DEA-C01)

> Source: [Official AWS DEA-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf)  
> Last verified: April 2026. Check the link above for any updates.

## Exam Structure

| Attribute | Detail |
|---|---|
| **Exam code** | DEA-C01 |
| **Format** | Multiple choice (1 correct) and multiple response (2+ correct) |
| **Total questions on screen** | 65 (50 scored + 15 unscored pilot questions — indistinguishable) |
| **Time** | 130 minutes (2 hrs 10 min) |
| **Passing score** | 720 out of 1000 (scaled scoring) |
| **Cost** | $150 USD |
| **Language** | English, Japanese, Korean, Simplified Chinese |
| **Delivery** | Pearson VUE (test center or online proctored) |
| **Validity** | 3 years |

## Exam Domains and Weighting

| Domain | Weight | What It Covers |
|---|---|---|
| **1. Data Ingestion and Transformation** | 34% | Getting data in, transforming it, ETL/ELT pipelines |
| **2. Data Store Management** | 26% | Storage selection, data modeling, schema management, catalog |
| **3. Data Operations and Support** | 22% | Automation, monitoring, orchestration, troubleshooting |
| **4. Data Security and Governance** | 18% | IAM, encryption, compliance, data quality, lineage |

### What This Means for You

- **Domain 1 is king** — over a third of the exam. This is Glue, Kinesis, MSK, EMR, Lambda, Step Functions, data formats, partitioning.
- **Domain 2** — S3, Redshift, DynamoDB, RDS, Lake Formation, Glue Data Catalog. You already know S3 and DynamoDB basics, so this is partially covered.
- **Domain 3** — CloudWatch, CloudTrail, EventBridge, Step Functions, troubleshooting patterns. Operational stuff.
- **Domain 4** — IAM policies, KMS encryption, Lake Formation permissions, VPC endpoints, compliance. This is where AWS newcomers lose points.

## Highest-Yield Topics (For Your Profile)

Since you already understand data engineering patterns, here's what will actually move the needle:

### Must-Know (Will Appear Repeatedly)
1. **AWS Glue** — ETL jobs, crawlers, Data Catalog, job bookmarks, Glue Studio, Glue DataBrew
2. **Amazon Kinesis** — Data Streams vs Data Firehose vs Data Analytics — when to use which
3. **Amazon Redshift** — Spectrum, COPY command, distribution styles, sort keys, materialized views
4. **Amazon S3** — storage classes, lifecycle policies, partitioning strategies, S3 Select
5. **AWS Lake Formation** — permissions model, data lake security, fine-grained access
6. **IAM** — policies, roles, cross-account access, service-linked roles
7. **AWS Step Functions** — orchestration patterns, error handling
8. **Data formats** — Parquet vs ORC vs Avro vs JSON, compression (Snappy, GZIP, LZO, ZSTD)

### Important (Will Appear Several Times)
9. **Amazon Athena** — querying S3, partition projection, CTAS, workgroups
10. **Amazon EMR** — when to use vs Glue, Spark on EMR, EMRFS
11. **Amazon MSK** — Kafka on AWS, MSK Connect, MSK Serverless
12. **Amazon EventBridge** — event-driven patterns, scheduling
13. **Amazon CloudWatch** — metrics, logs, alarms, dashboards
14. **AWS CloudTrail** — audit logging, data events vs management events
15. **AWS KMS** — encryption at rest, envelope encryption, key policies

### Nice-to-Know (1-3 Questions)
16. **Amazon DynamoDB** — streams, TTL, global tables (you have basics already)
17. **Amazon RDS/Aurora** — read replicas, Multi-AZ, Aurora Serverless
18. **AWS Lambda** — event sources, concurrency, DLQ
19. **VPC** — endpoints, PrivateLink, security groups for data services
20. **Amazon QuickSight** — basic BI concepts, SPICE

## Pass vs Nice-to-Know

| Focus Level | Topics | Exam Impact |
|---|---|---|
| **Must pass** | Glue, Kinesis, Redshift, S3, Lake Formation, IAM, Step Functions | ~60% of questions |
| **Should know** | Athena, EMR, MSK, EventBridge, CloudWatch, KMS | ~25% of questions |
| **Nice to know** | DynamoDB streams, RDS/Aurora, QuickSight, VPC details | ~15% of questions |

## Question Style

The exam is heavily **scenario-based**. Expect questions like:

> "A company ingests 500 GB of JSON data daily from IoT devices. The data must be available for ad-hoc SQL queries within 15 minutes of arrival. The solution must minimize operational overhead. Which combination of services should a data engineer use?"

You need to:
1. Identify the requirements (latency, volume, query pattern, cost, operational overhead)
2. Map to the right AWS service combination
3. Eliminate wrong answers based on constraints

The exam tests **service selection judgment**, not deep implementation details.
