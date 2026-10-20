# Commonly confused pairs — the discriminating fact
| Pair | Discriminator |
|---|---|
| KDS vs Firehose | KDS = replayable stream you consume; Firehose = managed delivery, ≥60 s buffer ✓, no replay |
| KDS vs MSK | KDS = AWS-native, shards, simple ops; MSK = Kafka API/ecosystem, partitions |
| KDS vs SQS | KDS = ordered replayable log, many consumers; SQS = delete-on-process queue, DLQ |
| SQS vs SNS | pull queue vs push pub/sub; combine = fan-out |
| SNS vs EventBridge | simple fan-out/high throughput vs rules, filtering, SaaS/AWS event sources, schedules |
| Standard vs FIFO SQS | ordering + dedupe (300 TPS/API ✓ per partition) vs near-unlimited |
| EFO vs shared consumers | EFO own 2 MB/s per consumer per shard (push, ≤20/50 ✓) vs 2 MB/s shared (pull) ✓ |
| Step Functions Standard vs Express | 1 y/exactly-once/history 90 d ✓ vs 5 min/high-volume ✓ |
| Step Functions vs MWAA | serverless AWS-native JSON/ASL vs Airflow Python DAGs, always-on env |
| Glue workflow vs Step Functions | Glue-only chain vs any service |
| Glue vs EMR | serverless ETL vs cluster control |
| Glue crawler vs DDL vs partition projection | auto-infer (cost/time) vs explicit vs computed partitions (no crawl) |
| MSCK REPAIR vs ADD PARTITION | scan all Hive-style prefixes vs register specific partition |
| Glue bookmarks vs Iceberg incremental | job-level processed tracking vs table snapshots |
| DynamicFrame vs DataFrame | flexible/choice types vs strict Spark schema |
| Athena vs Redshift | serverless pay-per-scan ad hoc vs warehouse for repeated heavy/BI |
| Spectrum vs Athena | Redshift querying S3 (join with local tables) vs standalone |
| Spectrum vs federated query | S3 external tables vs live RDS/Aurora |
| Redshift data sharing vs COPY/UNLOAD | live, no copy vs moved data |
| Concurrency scaling vs elastic resize | extra read clusters for bursts vs change node count |
| KEY vs ALL vs EVEN | co-locate big join, replicate small dim, round-robin |
| Compound vs interleaved sort key | leading-prefix range vs equal-weight multi-column |
| COPY vs INSERT | parallel bulk vs row-by-row (slow) |
| DynamoDB GSI vs LSI | any PK, async, own capacity, anytime vs same PK, 10 GB, strong reads, creation-time |
| DynamoDB Streams vs KDS for DDB | 24 h, ≤2 readers ✓ vs longer retention, many consumers |
| DynamoDB vs Keyspaces vs DocumentDB | AWS-native KV vs Cassandra API vs Mongo API |
| MemoryDB vs DynamoDB DAX | durable primary Redis-API DB vs cache in front of DDB |
| RDS vs Aurora | engine-managed vs cloud-native (up to 15 replicas ~, faster failover, Global DB, pgvector) |
| Aurora vs Redshift | OLTP vs OLAP |
| Neptune vs DocumentDB | graph relationships vs documents |
| DMS vs DataSync | DB (CDC) vs file sync |
| DataSync vs Transfer Family | agent-based bulk online sync vs SFTP/FTPS endpoint for partners |
| DataSync vs Snow | network transfer vs offline appliance |
| AppFlow vs DMS | SaaS vs database |
| Zero-ETL vs DMS | managed replication to Redshift/lakehouse (supported sources ✓) vs general-purpose |
| S3 Standard-IA vs One Zone-IA vs Intelligent-Tiering | multi-AZ infrequent vs single-AZ re-creatable vs unknown pattern |
| Glacier IR vs FR vs DA | ms, 90 d ✓ / min-hours, 90 d ✓ / 12–48 h, 180 d ✓ |
| S3 Lifecycle vs DynamoDB TTL | storage tier/expire vs item expiry (free) |
| SSE-S3 vs SSE-KMS vs SSE-C vs client-side | AWS key, audited CMK, customer key per request, encrypt before upload |
| KMS key policy vs IAM | key policy required root; IAM only if key policy delegates |
| AWS-managed vs customer-managed key | no cross-account / limited control vs full |
| Secrets Manager vs Parameter Store | rotation vs cheap config |
| Gateway vs Interface endpoint | S3/DDB route-table, free vs ENI/PrivateLink, paid |
| Security group vs NACL | stateful allow vs stateless allow/deny subnet |
| IAM vs Lake Formation | coarse identity/resource vs table/column/row/cell central |
| LF named-resource vs LF-tag grants | per object vs scalable attribute |
| Macie vs Glue sensitive detection vs DataBrew | S3 discovery vs in-ETL detect/mask vs visual masking |
| CloudTrail vs CloudWatch vs Config | API audit vs metrics/logs vs resource config state |
| CloudTrail trail vs CloudTrail Lake | S3 JSON logs (Athena) vs managed SQL event store |
| CloudWatch Logs Insights vs Athena vs OpenSearch | quick log query vs S3 log lake SQL vs search/dashboards |
| QuickSight(Quick) SPICE vs Direct Query | in-memory import vs live |
| DataBrew vs Data Wrangler | Glue visual recipes vs SageMaker notebook prep |
| Glue Data Quality vs Deequ | managed DQDL vs OSS library on Spark |
| SageMaker Catalog vs Glue Data Catalog | business catalog/governance vs technical metadata |
| pgvector HNSW vs IVF | high-recall graph, more memory vs cluster-based, cheaper, lower recall |
| Bedrock KB vs DIY RAG | managed ingest/chunk/embed/retrieve vs custom pipeline |
| Provisioned vs on-demand/serverless | steady cost-optimised vs spiky least-ops |
| Lambda reserved vs provisioned concurrency | cap/guarantee vs pre-warmed |
| SAM vs CDK vs CloudFormation | CFN extension for serverless vs code that synthesises CFN vs declarative base |
| Kinesis Data Analytics vs Managed Service for Apache Flink | same service, renamed |
