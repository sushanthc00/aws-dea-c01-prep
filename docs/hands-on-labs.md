# Optional hands-on labs (6) — low-cost, with clean-up
**Optional.** With ~12 days left, do at most 1–2 (suggest Lab 1 and Lab 4) and only if they don't cost study time. All commands are **untested snippets** — adapt names/Regions. **Cost warning:** AWS free-tier eligibility, allowances and prices change and differ per account/Region; check the Billing console and the service pricing pages before starting [free-tier terms NOT verified here]. Use a throwaway sandbox account, set an AWS Budget alert (e.g., USD 5), use one Region (e.g., `ap-south-1` or `us-east-1`), and always run the clean-up block. Never use production credentials or data; use synthetic data only.

Common setup
```bash
export AWS_REGION=us-east-1; export ACCT=$(aws sts get-caller-identity --query Account --output text)
export B=dea-lab-$ACCT-$RANDOM; aws s3 mb s3://$B
```

## Lab 1 — S3 + Glue Catalog + Athena: CSV → partitioned Parquet (skills 1.2.6, 2.4.5, 3.1.7, 2.2.x)
**Cost:** pennies (tiny data; Athena bills per data scanned; use a workgroup scan limit).
1. Create `orders.csv` (a few thousand synthetic rows with `order_id,customer_id,amount,order_date`), upload to `s3://$B/raw/orders/`.
2. In Athena: `CREATE DATABASE lab; CREATE EXTERNAL TABLE lab.orders_csv (...) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION 's3://$B/raw/orders/' TBLPROPERTIES ('skip.header.line.count'='1');`
3. CTAS to Parquet partitioned by month: `CREATE TABLE lab.orders_pq WITH (format='PARQUET', parquet_compression='SNAPPY', partitioned_by=ARRAY['m'], external_location='s3://$B/curated/orders/') AS SELECT order_id, customer_id, amount, date_format(date(order_date),'%Y-%m') AS m FROM lab.orders_csv;`
4. Compare "Data scanned" for `SELECT sum(amount) …` on CSV vs Parquet with `WHERE m='2026-01'`. Add `rolling average` window query. Create a view.
5. Create a **workgroup** with per-query data limit and an SNS alarm (skill 3.1.7 context).
**Verify:** Parquet query scans far fewer bytes. **Clean-up:** `DROP TABLE`s, `DROP DATABASE lab`, `aws s3 rb s3://$B --force`, delete workgroup.

## Lab 2 — Kinesis Data Streams → Lambda / Firehose → S3 (skills 1.1.1, 1.1.7, 1.1.9–1.1.10)
**Cost:** a stream accrues **hourly charges while it exists** (on-demand has a per-stream hourly price + data) — finish within an hour and delete. Firehose bills per GB ingested.
1. `aws kinesis create-stream --stream-name lab-clicks --stream-mode-details StreamMode=ON_DEMAND`
2. Put records: `aws kinesis put-record --stream-name lab-clicks --partition-key u1 --data $(echo '{"u":"u1","p":"/home"}' | base64)` in a loop; try `put-records` batch.
3. Create a Firehose delivery stream (Source: Kinesis stream, Destination: S3 `s3://$B/firehose/`, buffer 60 s/1 MB, optional Parquet conversion needs a Glue table).
4. Create a tiny Lambda (print records) with an event source mapping: batch size 100, `--bisect-batch-on-function-error`, on-failure SQS destination; deliberately throw on one record and watch retries/bisect (skill 1.1.7).
5. Register an enhanced fan-out consumer and view metrics (`GetRecords.IteratorAgeMilliseconds`, `WriteProvisionedThroughputExceeded`).
**Verify:** files appear in S3 after ≥ 60 s; poison record lands in the SQS destination. **Clean-up:** delete event source mapping, Lambda, Firehose stream, Kinesis stream, SQS queue, S3 objects.

## Lab 3 — Glue crawler + ETL job with bookmarks + Data Quality (skills 2.2.3, 1.1.3, 3.4.1–3.4.2, 1.2.7)
**Cost:** Glue bills DPU-hours per job run (minimum workers apply; per-second billing with a minimum duration ~); keep to 2 G.1X workers, Flex execution class for the run, a short timeout (e.g., 10 min), no schedules. Crawler also bills DPU-time.
1. Create a Glue database and **crawler** over `s3://$B/raw/orders/` with schema-change policy **Log**.
2. Create a Spark job (Glue 5.1 default): read from the catalog with `push_down_predicate`, `transformation_ctx`, write Parquet partitioned; enable **job bookmarks**; call `job.commit()`.
3. Add an **Evaluate Data Quality** step with `Rules = [ IsComplete "order_id", IsUnique "order_id", Completeness "customer_id" > 0.98, ColumnValues "amount" > 0 ]`; configure fail-on-error; inject a bad row and observe failure.
4. Run twice: second run should process **no new data** (bookmark). Reset the bookmark and rerun.
5. Enable continuous logging + Spark UI; read the job run's CloudWatch logs.
**Verify:** bookmark behaviour, DQ failure message. **Clean-up:** delete job, crawler, database, script/temp S3 objects, CloudWatch log groups.

## Lab 4 — Lake Formation column-level permissions with Athena (skills 4.2.4, 4.2.5, 4.5.2)
**Cost:** Lake Formation itself has no extra charge ✓ (per AWS announcements); Athena scan costs only. Use the Lab 1 Parquet table.
1. Create two IAM roles/users: `analyst` and `scientist` (Athena + Glue + S3 results bucket permissions only; **no direct S3 read** on the data prefix).
2. Lake Formation → Data lake administrators (add yourself); **register** `s3://$B/curated/` with the LF service-linked role; in Data Catalog settings ensure `IAMAllowedPrincipals` no longer grants Super on `lab.orders_pq` (revoke).
3. Grant `scientist` SELECT on all columns; grant `analyst` SELECT on all columns **except** `customer_id` (column filter).
4. Query as each principal in Athena; confirm `analyst` gets `COLUMN_NOT_FOUND`/denied for `customer_id`.
5. Optional: create **LF-tags** (`pii=true` on `customer_id`) and re-grant by tag expression; try **hybrid access mode** on the location and an opted-in vs non-opted-in principal.
**Verify:** column visibility differs by principal. **Clean-up:** revoke grants, deregister location, delete tags/roles, drop tables, delete bucket.

## Lab 5 — DynamoDB modeling: GSI, TTL, PITR, streams (skills 2.4.1, 2.3.4, 2.3.6, 1.1.1)
**Cost:** on-demand pennies for a few items; PITR adds a small storage charge — disable/delete after.
1. Create table `orders` (PK `customerId`, SK `orderDate`) on-demand.
2. Add a **GSI** (PK `orderId`) and another (PK `status`, SK `orderDate`); try to add an LSI to the existing table and observe it's creation-time only (create a new table to test).
3. Enable **TTL** on `expireAt` (epoch seconds); insert items with past/future expiry; observe deletion lag.
4. Enable **PITR**, **Streams** (NEW_AND_OLD_IMAGES) and read a stream record via CLI; run `query` by customer (newest first, `--no-scan-index-forward`) and via GSI.
5. Practice conditional write (optimistic locking): `--condition-expression "attribute_not_exists(orderId) OR version = :v"`.
**Verify:** Query vs Scan consumed capacity; GSI queries across customers. **Clean-up:** delete tables, disable PITR.

## Lab 6 — Step Functions orchestration: S3 event → Glue → Athena → SNS with Retry/Catch (skills 1.3.1–1.3.4, 3.3.3)
**Cost:** Standard workflows are billed per state transition (a few cents at most); the Glue job cost from Lab 3 applies.
1. Create an SNS topic + email subscription.
2. State machine (see `guide/D1-ingestion-transformation/1.3-orchestration.md` §10): `glue:startJobRun.sync` with Retry (IntervalSeconds, BackoffRate, MaxAttempts), `athena:startQueryExecution.sync`, Catch → SNS publish.
3. EventBridge rule: S3 `Object Created` on `raw/` → target the state machine (enable EventBridge notifications on the bucket).
4. Upload a file; watch the execution graph; force a failure (bad job argument) to see Retry then Catch and the SNS email.
5. Add a **Wait for callback** (`.waitForTaskToken`) state and complete it manually with `send-task-success`.
**Verify:** execution history, failure branch. **Clean-up:** delete state machine, rule, topic, IAM roles, Glue job, bucket notifications.

## Final clean-up and cost check
`aws resourcegroupstaggingapi get-resources --tag-filters Key=lab` (if you tagged) or review each service console in the lab Region; Cost Explorer next day; delete the Budget if no longer needed. Keep the account free of long-lived access keys.
