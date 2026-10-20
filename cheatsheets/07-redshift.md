# Redshift cheat sheet
✓ = verified via What's New headlines · ~ = established doc knowledge, re-check in Phase 3/5.

## Deployment
| | Provisioned (RA3 ~) | Serverless |
|---|---|---|
| Use | steady, predictable, reserved pricing | spiky/unpredictable, least ops, per-RPU-second |
| Scale | resize / elastic resize; **concurrency scaling** for read bursts | auto; base RPU capacity; 3-yr reservation up to 45 % savings ✓ |
| Storage | RA3 managed storage (S3-backed), compute/storage decoupled ~ | managed |
Redshift Spectrum = query S3 external tables (Glue catalog) without loading · Federated query = RDS/Aurora PostgreSQL/MySQL live · Data sharing = live access across clusters/serverless workgroups/accounts/Regions without copying (producer/consumer); ✓ now supports **writes** (INSERT/UPDATE) as well as reads, not read-only · Streaming ingestion = materialized view over KDS/MSK ✓ (concurrency scaling for KDS refresh ✓) · zero-ETL from Aurora/RDS/DynamoDB ~ · Auto-copy from S3 ~ · Min TLS 1.2 ✓ · scalar Python UDF end of support after 2026-06-30 → Lambda UDF ✓.

## Table design (skill 2.4.1)
| Distribution | When |
|---|---|
| **AUTO** (default) | let Redshift choose (ALL small → EVEN/KEY as it grows) |
| **KEY** | large fact+dimension joined on same column → co-locate; watch skew |
| **ALL** | small, slowly-changing dimension tables |
| **EVEN** | no join / no clear key |
Sort keys: **compound** (default; prefix filters, range on leading col), **interleaved** (equal weight to multiple cols; slower loads; rarely best), AUTO. Zone maps skip blocks. Compression encodings: AUTO/`ANALYZE COMPRESSION`. Primary/foreign keys are **informational only** (not enforced) ~. `VACUUM` (auto), `ANALYZE` (auto), automatic table optimization ~.

## Loading & unloading (2.3.1)
- `COPY` from S3 (also DynamoDB, EMR, SSH), parallel across slices → **split input into multiple files, ideally a multiple of slice count, 1–125 MB compressed each ~**; use manifest; IAM role; `COMPUPDATE`, `STATUPDATE` options. Single huge file = single slice (slow). Load Parquet/ORC directly ~.
- `UNLOAD` to S3 (Parquet, partitioned, parallel by default); `INSERT ... SELECT`, CTAS, `MERGE` ~.
- Staging-table upsert: load → stage → delete+insert in transaction (older) or MERGE.
- Don't use many single-row INSERTs.

## Performance & troubleshooting
| Symptom | Fix |
|---|---|
| Queries queueing | **WLM**: automatic WLM + query priorities; Concurrency Scaling; short query acceleration (SQA); query monitoring rules (abort/log long queries) |
| Slow joins/DISTRIBUTE steps | wrong dist key → KEY on join col or ALL for small dims; check `SVL_QUERY_SUMMARY`/`EXPLAIN` for DS_BCAST/DS_DIST |
| Disk full / spilled | heavy temp; add nodes, RA3, fix skew, reduce columns |
| Stale stats / unsorted | ANALYZE/VACUUM (auto does it) |
| Dashboard repeat queries | **materialized views** (auto refresh, auto query rewrite ~), result caching |
| Cold historical data | UNLOAD to S3 Parquet + Spectrum |
| Locks (2.1.6) | `STV_LOCKS`, `SVV_TRANSACTIONS`, `PG_TERMINATE_BACKEND`; DDL/TRUNCATE take locks; long open transactions block |
Monitoring: CloudWatch (CPUUtilization, PercentageDiskSpaceUsed, ConcurrencyScalingSeconds ~), SYS_* monitoring views, audit logging to S3/CloudWatch, Query Editor v2.

## Security (4.2.3, 4.3, 4.5.1)
IAM roles for COPY/UNLOAD/Spectrum; database users/groups/**roles** (RBAC) with GRANT; **row-level security**, **dynamic data masking** ~, column-level GRANT; KMS encryption at rest (cluster), SSL in transit (require_ssl); VPC, enhanced VPC routing (force traffic through VPC/endpoints); IAM Identity Center/federation; secrets via Secrets Manager; Lake Formation governs Spectrum/data-lake & Redshift data sharing with LF ~. Data sharing permission: producer `GRANT USAGE ON DATASHARE`, consumer creates DB from share; cross-account needs `authorize` + `associate` ~.

## Snippet (untested)
```sql
COPY sales FROM 's3://lake/curated/sales/dt=2026-10-19/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftCopyRole'
FORMAT AS PARQUET;

UNLOAD ('SELECT * FROM sales WHERE sale_date < ''2025-01-01''')
TO 's3://lake/archive/sales/' IAM_ROLE '...' FORMAT PARQUET PARTITION BY (sale_date);

CREATE TABLE fact_sales (sale_id BIGINT, cust_id INT, sale_date DATE, amt DECIMAL(12,2))
DISTSTYLE KEY DISTKEY(cust_id) SORTKEY(sale_date);
```
