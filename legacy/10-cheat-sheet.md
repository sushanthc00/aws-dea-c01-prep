# 1-Page Cheat Sheet — AWS DEA-C01

## Service Selection Quick Reference

| Need | Use This |
|---|---|
| Serverless ETL on S3 | **Glue ETL** |
| Schema discovery | **Glue Crawler** |
| Central metadata store | **Glue Data Catalog** |
| Serverless SQL on S3 | **Athena** |
| Data warehouse | **Redshift** |
| Query S3 from Redshift | **Redshift Spectrum** |
| Bulk load into Redshift | **COPY command** |
| Export from Redshift to S3 | **UNLOAD command** |
| Real-time streaming (custom) | **Kinesis Data Streams** |
| Managed delivery to S3/Redshift | **Kinesis Data Firehose** |
| Real-time analytics (Flink) | **Kinesis Data Analytics** |
| Kafka on AWS | **Amazon MSK** |
| Complex Spark with full control | **Amazon EMR** |
| Workflow orchestration | **Step Functions** |
| Event-driven triggers/scheduling | **EventBridge** |
| Lightweight compute (<15 min) | **Lambda** |
| Data lake governance | **Lake Formation** |
| PII detection | **Amazon Macie** |
| Encryption key management | **AWS KMS** |
| API audit logging | **CloudTrail** |
| Operational monitoring | **CloudWatch** |
| SaaS data ingestion | **Amazon AppFlow** |
| SFTP to S3 | **AWS Transfer Family** |
| Database migration + CDC | **AWS DMS** |
| No-code data prep | **Glue DataBrew** |
| Data quality rules | **Glue Data Quality (DQDL)** |
| Low-latency key-value | **DynamoDB** |
| BI dashboards | **QuickSight** |

## Critical Decision Trees

### Streaming: Kinesis Streams vs Firehose vs MSK
- Need custom processing + replay? → **Streams**
- Just deliver to S3/Redshift/OpenSearch? → **Firehose** (near real-time)
- Already using Kafka? → **MSK**
- Need windowed aggregations? → **Kinesis Data Analytics (Flink)**

### ETL: Glue vs EMR vs Lambda
- Simple ETL, serverless? → **Glue**
- Complex Spark, custom libs, multi-framework? → **EMR**
- Small data, quick transform (<15 min, <10 GB)? → **Lambda**
- Small data, Python/pandas? → **Glue Python Shell**

### Query: Athena vs Redshift vs Redshift Spectrum
- Ad-hoc SQL on S3, no infra? → **Athena**
- Complex analytics, high concurrency, joins? → **Redshift**
- Extend Redshift queries to S3? → **Spectrum**

## Encryption Quick Reference
| Type | Key Management | Audit | Use When |
|---|---|---|---|
| SSE-S3 | AWS | No | Default, simplest |
| SSE-KMS | You control | Yes (CloudTrail) | Need audit + rotation control |
| SSE-C | You provide | No | Must manage own keys |

## Redshift Distribution Styles
| Style | Use When |
|---|---|
| KEY | Large tables frequently joined on that column |
| ALL | Small dimension tables (<few million rows) |
| EVEN | No clear join pattern |
| AUTO | Let Redshift decide |

## Data Format Selection
| Format | Type | Best For |
|---|---|---|
| Parquet | Columnar | Analytics, Athena, Spectrum |
| ORC | Columnar | Hive/EMR workloads |
| Avro | Row | Streaming, schema evolution |
| JSON | Row | Raw ingestion, APIs |

## Key Numbers to Remember
- Lambda: 15 min timeout, 10 GB memory
- Firehose buffer: 60-900 sec, 1-128 MB
- Kinesis retention: 24 hrs default, up to 365 days
- Kinesis shard: 1 MB/s in, 2 MB/s out
- Redshift COPY: best with files = multiple of slices
- Athena: charges per TB scanned
- Step Functions Standard: up to 1 year
- Step Functions Express: up to 5 minutes
