# Domain 3 — Operations & Support (22 %) — one-pager
Task map: 3.1 automate · 3.2 analyze · 3.3 maintain/monitor · 3.4 data quality.

## Monitoring toolbox
| Need | Tool |
|---|---|
| Metrics/alarms/dashboards | CloudWatch Metrics + Alarms → SNS / EventBridge / Auto Scaling |
| Application/job logs | CloudWatch Logs (retention, metric filters, subscription filters → Firehose/Lambda/OpenSearch); **Logs Insights** for ad-hoc queries |
| API audit (who did what) | CloudTrail (management events default; data events opt-in ~); CloudTrail Lake = SQL over events, central (4.4.3); Event history 90 d ~ |
| Config history/compliance | AWS Config (rules, timeline) |
| Query logs at scale | S3 + Athena; OpenSearch for search/dashboards; EMR for huge log volumes (4.4.5) |
| Workflow state | Step Functions execution history (Standard 90 d ✓), MWAA task logs/CloudWatch, Glue run logs/Spark UI |
| Cost | Cost Explorer, Budgets, cost allocation tags |
| Dashboards | Managed Grafana (in scope), Amazon Quick |
Alerts (3.3.3): CloudWatch alarm → SNS; EventBridge rule on state change (Glue job FAILED, Step Functions failure, DMS task, Redshift) → SNS/Lambda/SQS.

## Symptom → cause → fix
| Symptom | Fix |
|---|---|
| Kinesis `ProvisionedThroughputExceeded` (write) | hot shard/too little capacity → more shards/on-demand, better partition key, batch+backoff |
| Kinesis read throttle / rising `IteratorAge` | EFO, more shards, faster consumer, Lambda parallelization factor |
| Lambda throttles (429) / concurrency | reserved/provisioned concurrency, raise quota ✓ default 1,000, SQS buffer, reduce batch duration; sync invoke limit 10× concurrency ✓ |
| Lambda timeout | >15 min ✓ → Step Functions/Glue/Batch; raise memory (CPU) |
| S3 503 Slow Down | more prefixes (3,500/5,500 per prefix ✓), retries with backoff, avoid key-name hotspots |
| S3 access denied w/ KMS | role lacks kms perms / key policy; SSE-KMS request throttling → Bucket Keys ~ |
| Glue OOM / skew / small files / timeout | see 09-glue |
| Glue job stuck/slow crawler | targeted crawl, incremental, partition projection |
| Redshift queue waits | WLM auto, concurrency scaling, SQA, MV; see 07-redshift |
| Athena slow/expensive | Parquet/ORC, partition, compress, avoid SELECT *, CTAS compaction, workgroup data-scan limits, partition projection; `HIVE_PARTITION_SCHEMA_MISMATCH`, `TooManyRequestsException` ✓ queued query limit → capacity reservation |
| EMR step fails / slow | CloudWatch + EMR logs to S3, YARN memory settings, instance fleets/Spot interruption, managed scaling; extended support for old releases ✓ |
| MWAA DAG not appearing/failing | DAG parse errors in scheduler logs, requirements.txt/plugins in S3, execution role, env class size, VPC/NAT for pip |
| Step Functions history limit | 25,000 events ✓ → split, Distributed Map, child executions |
| DMS task lag/failure | CDC latency metrics `CDCLatencySource/Target`, replication instance size, LOB settings, logging, validation ~ |
| DynamoDB throttling | on-demand / auto scaling, hot partition key, adaptive capacity, retry |
| Data skew (3.4.5) | salting, repartition, broadcast join, AQE, choose better keys |

## Analysis (3.2)
- Athena: SQL on S3; **workgroups** (cost control, per-team limits); CTAS/views/UNLOAD; **Spark notebooks (3.2.4)** for interactive PySpark without clusters; federated queries; provisioned **capacity reservations** (≥4 DPU ✓~) vs serverless pay-per-scan (3.2.5 trade-off: predictable steady heavy → provisioned; spiky/ad hoc → serverless).
- Quick (QuickSight): SPICE import (fast, scheduled refresh, capacity limits) vs Direct Query; row-level security; embedding; ML insights.
- DataBrew: visual profile/clean; Data Wrangler (SageMaker): visual prep in notebooks; Jupyter in SageMaker Unified Studio; Lambda for cleaning.
- SQL (3.2.3/3.2.6): window functions `AVG(x) OVER (PARTITION BY k ORDER BY ts ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` (rolling average), `GROUP BY`, `PIVOT`/conditional aggregation, `ROLLUP/CUBE`; views (Athena views in catalog; Redshift views/MVs/late-binding views ~).
- Provisioned vs serverless trade-offs: serverless = no capacity planning, scale to zero, higher unit cost at steady load; provisioned = cheaper at predictable high utilization, reservation discounts (Redshift 3-yr 45 % ✓).

## Data quality (3.4)
- During processing: Glue Data Quality (DQDL), Deequ on EMR/Spark, Lambda checks, Step Functions Choice on results, quarantine bad records to “dead-letter” S3 prefix.
- Rules: completeness, uniqueness, range/pattern, referential, freshness, row count; DataBrew rulesets; alert via EventBridge → SNS.
- Consistency (3.4.3): compare counts/checksums source vs target (DMS validation ~), idempotent upserts, Iceberg ACID.
- Sampling (3.4.4): random, stratified, systematic, reservoir for streams; DataBrew profile sample size; Athena `TABLESAMPLE`~.
- Skew (3.4.5): see above.

## Automation (3.1)
Orchestrate (Step Functions/MWAA) ✓, troubleshoot managed workflows (3.1.2) — MWAA logs, SFN console/X-Ray ✗(X-Ray out of scope ✓), SDK calls (boto3 retries, pagination, waiters), EventBridge Scheduler (cron/rate, one-time, flexible windows ~), Lambda triggered by S3/SQS/Kinesis/DDB Streams/EventBridge, data APIs (API Gateway).

## Trap list
- CloudTrail = API calls; CloudWatch = metrics/logs; Config = resource configuration state.
- Athena quotas count queued queries ✓; add retries.
- Glue bookmarks don't help if the job doesn't `commit()`.
