# AWS Glue cheat sheet
✓ verified (exam/WN) · ~ established, re-check Phase 3. Current version: **Glue 5.1** (Spark 3.5.6, Python 3.11, Scala 2.12.18; Iceberg 1.10.0, Hudi 1.0.2, Delta 3.3.2) ✓.

## Components
| Component | What | Exam hook |
|---|---|---|
| Data Catalog | Hive-metastore-compatible metadata (databases, tables, partitions, connections); used by Athena, Redshift Spectrum, EMR, LF | one per Region/account; cross-account via LF/RAM; **technical** catalog (skill 2.2.2) vs business catalog (SageMaker Catalog, 2.2.6) |
| Crawlers | scan sources, infer schema, create/update tables & partitions; classifiers; schedule or event (S3 events) ~ | cost/time on large S3 → use **partition projection** or `ALTER TABLE ADD PARTITION`/`MSCK REPAIR`, or crawl only new folders (incremental crawl ~) |
| ETL jobs | Spark (batch/streaming), Python shell (small), Ray ~ ; script via Studio visual, notebooks, code | workers G.1X/G.2X/…; auto scaling; **Flex** execution class = cheaper, non-urgent, may start later ~ |
| Job bookmarks | track processed data for incremental loads (S3, JDBC) | enable → no reprocessing; reset to rerun; needs `transformation_ctx` ~ |
| DynamicFrame | schema-flexible; `ResolveChoice`, `ApplyMapping`, `Relationalize` (nested JSON → tables) | vs Spark DataFrame: use for messy/evolving schemas |
| Workflows/triggers | chain crawlers/jobs: on-demand, scheduled, conditional, EventBridge | simple Glue-only DAG; for cross-service use Step Functions |
| Data Quality | DQDL rulesets (`Completeness "col" > 0.95`, `IsUnique`, `ColumnValues`…), evaluate in jobs or on catalog tables; results to CloudWatch/S3; Deequ under the hood ~ | skill 3.4.1/3.4.2 |
| DataBrew | no-code recipes, profile jobs, data quality rules | skill 3.1.6/3.4.2 |
| Schema Registry | Avro/JSON/Protobuf schemas for KDS/MSK/Flink with compatibility modes ~ | schema evolution for streams |
| Sensitive data detection | detect/mask/hash PII in jobs ~ | complements Macie (S3) |
| Connections | JDBC/ODBC, Kafka, Marketplace, VPC (SG + subnet) | needs **self-referencing security group** + S3 gateway endpoint for VPC jobs ~ |
| Zero-ETL | DynamoDB, Oracle DB@AWS, SaaS sources → lakehouse/Redshift ✓ (WN) | |

## Job tuning & troubleshooting
| Symptom | Likely cause | Fix |
|---|---|---|
| `OutOfMemoryError` driver | `collect()`, huge broadcast, too many small files listing | more memory (G.2X+), `groupFiles`/`groupSize` for small files, avoid collect, push down predicates |
| OOM executor / slow stage | **data skew** | salting keys, `repartition`, AQE skew join (Glue 3.0+ ~), broadcast small side |
| Too many small files | many tiny S3 objects/frequent micro-batches | `groupFiles=inPartition`, compaction job, Firehose larger buffer, Iceberg compaction |
| Full scan though partitioned | no pushdown | `push_down_predicate` on partition keys; partition columns in WHERE |
| Reprocessing everything | bookmarks off / reset | enable bookmarks + `transformation_ctx` |
| Job timeout / DPU underuse | wrong worker count | enable auto scaling, check job metrics (`glue.driver.*`, `glue.ALL.system.cpuSystemLoad`) & Spark UI |
| `AccessDenied` S3/KMS | job role lacks `kms:Decrypt`/bucket access | fix role / key policy |
| Cannot reach JDBC in VPC | no NAT / endpoints / SG | NAT for internet, VPC endpoints, self-ref SG |
| Crawler wrong schema | mixed schemas in one prefix | separate prefixes; exclude patterns; custom classifier |
Observability: CloudWatch Logs (continuous logging), job metrics, **Spark UI** + history server, job run insights ~; alerts via EventBridge (job state change) → SNS.

## Formats (see 06-formats)
CSV→Parquet via `write_dynamic_frame` with `format="parquet"`, `compression="snappy"`; partition on low-cardinality filter columns (date).

## Glue vs others
| | Glue | EMR | Lambda | Athena CTAS |
|---|---|---|---|---|
| Ops | serverless | cluster mgmt (Serverless option) | none | none |
| Duration | long | long | ≤15 min ✓ | ≤ DML timeout ✓ |
| Control | medium | high | low | SQL only |
| Cost | DPU-hour (min billing per run ~) | EC2/Spot cheaper at scale | per ms | per TB scanned |
Pick Glue by default for “serverless ETL, least ops, catalog, bookmarks”; EMR for “custom frameworks / existing Spark with tuning / Spot / HBase/Presto”.

## Snippets (untested)
```python
# Glue Spark: read with pushdown + incremental via bookmarks, write partitioned Parquet
dyf = glueContext.create_dynamic_frame.from_catalog(
    database="sales", table_name="raw_orders",
    push_down_predicate="dt >= '2026-10-01'", transformation_ctx="src")
glueContext.write_dynamic_frame.from_options(
    frame=dyf, connection_type="s3",
    connection_options={"path": "s3://lake/curated/orders/", "partitionKeys": ["dt"]},
    format="parquet", format_options={"compression": "snappy"}, transformation_ctx="sink")
job.commit()   # required for bookmarks
```
```sql
-- DQDL example
Rules = [ IsComplete "order_id", IsUnique "order_id", ColumnValues "amount" > 0,
          Completeness "customer_id" > 0.98 ]
```
