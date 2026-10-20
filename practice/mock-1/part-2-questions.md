# Mock Exam 1 — Part 2 (Questions 23–44)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q23

A scheduled AWS Glue Spark job reads a growing S3 prefix and reprocesses every file on each run, causing duplicates downstream and rising cost. The team wants each run to process only new files.
What should be done?

A. Increase the number of workers so the full reload finishes faster and costs less overall.  
B. Run a crawler before each job run so the job knows which files are new.  
C. Enable job bookmarks, set transformation_ctx on sources and sinks, and call job.commit().  
D. Query the data with S3 Select so that only the matching objects are read.  

### Q24

New daily partitions (dt=YYYY-MM-DD) are written to S3 and are not visible to Athena queries until a crawler runs, causing delays and crawler costs. Partition values follow a predictable date pattern. The team wants the LEAST operational overhead.
What should be done?

A. Configure partition projection on the Athena table for the dt column.  
B. Run the Glue crawler every minute so new partitions are registered almost immediately.  
C. Run MSCK REPAIR TABLE from a Lambda function on an hourly schedule.  
D. Convert the table to an unpartitioned table so no partition registration is needed.  

### Q25

A Standard AWS Step Functions workflow iterates over 60,000 items using an inline Map state. After several hours the execution fails because it exceeds the execution history limit of 25,000 events.
What is the BEST fix?

A. Convert the state machine to an Express workflow, which has no execution history limit.  
B. Request an increase of the execution history limit through Service Quotas.  
C. Increase the Lambda timeout for each item so the iterations finish within fewer events.  
D. Use a Distributed Map state so each batch of items runs as a child workflow execution.  

### Q26

A company must find personally identifiable information (PII) stored in an S3 data lake and then ensure analysts querying with Athena cannot see PII columns.
Which TWO actions together meet these requirements? (Select TWO.)

A. Run Amazon Macie sensitive data discovery jobs on the buckets.  
B. Enable Amazon GuardDuty S3 protection.  
C. Tag PII columns in the Glue Data Catalog with a Lake Formation LF-tag and grant analysts access only to non-PII tag values.  
D. Enable S3 Versioning on the buckets.  
E. Enable an AWS Config managed rule for S3 encryption.  

### Q27

Clickstream events arrive in Kinesis Data Streams. They must be loaded into an Amazon Redshift cluster that is NOT publicly accessible within seconds to a few minutes, with the LEAST custom code.
Which solution is BEST?

A. Amazon Data Firehose delivering directly into the private Redshift cluster.  
B. A Redshift streaming ingestion materialized view that reads from the Kinesis stream.  
C. A Lambda function that reads the stream and issues single-row INSERT statements.  
D. AWS DMS with the Kinesis stream configured as a source endpoint.  

### Q28

Operational data lives in Amazon Aurora MySQL. Analysts need near-real-time analytics in Amazon Redshift, and the company wants to avoid building and operating ETL pipelines.
Which solution is BEST?

A. DMS full load and CDC to S3, then scheduled COPY into Redshift.  
B. A Glue job every 5 minutes.  
C. Lambda functions triggered by binlog events.  
D. An Amazon Aurora zero-ETL integration with Amazon Redshift.  

### Q29

A Lambda function needs read access to a 6 GB reference dataset that is refreshed by another process without redeploying the function. All concurrent invocations must see the latest data.
What is the MOST appropriate approach?

A. Mount an Amazon EFS file system to the function.  
B. Package the dataset in the function's deployment ZIP file and redeploy on every update.  
C. Put the dataset in a Lambda layer that is shared by all versions of the function.  
D. Store the dataset in an environment variable that the function reads at start.  

### Q30

An Amazon Quick (QuickSight) dashboard reads directly from Athena over a large S3 dataset. It is slow and expensive, but the data changes only once per day.
What should the data engineer do?

A. Use a larger Athena workgroup so the dashboard queries get more compute.  
B. Increase the Athena query timeout so the dashboard queries do not fail.  
C. Import the dataset into SPICE and schedule a daily refresh.  
D. Add more prefixes to the S3 bucket so the dashboard queries read in parallel.  

### Q31

A company will migrate an on-premises Oracle database to Amazon Aurora PostgreSQL with minimal downtime.
Which approach should the data engineer use?

A. AWS DataSync to copy the database files to the target Aurora cluster.  
B. DMS Schema Conversion for the schema, then AWS DMS full load plus CDC.  
C. An AWS Snowball Edge export and import of the database files.  
D. A Glue crawler that catalogs and copies the tables to Aurora.  

### Q32

A producer team has Redshift tables that a consumer team in another AWS account must query live, without copying data.
Which approach should be used?

A. Create a datashare on the producer, authorize the consumer account, and associate it on the consumer.  
B. UNLOAD the data to S3 every day and share the bucket with the consumer account.  
C. Create a cross-account IAM user in the producer cluster and share its credentials.  
D. Take a snapshot of the cluster and restore it into the consumer account.  

### Q33

An order-placed event must trigger three independent downstream systems. Each needs its own retries and a dead-letter queue, and a failure in one must not affect the others.
Which design is BEST?

A. One SQS queue that is read by all three downstream systems.  
B. A single Lambda function that calls the three systems in sequence with try/catch.  
C. Three Kinesis streams that the producer writes to, one per downstream system.  
D. An SNS topic with three SQS queue subscriptions, each with its own dead-letter queue.  

### Q34

Auditors must identify which IAM principal deleted specific objects from an S3 bucket. An existing CloudTrail trail does not show object-level deletions.
What should be done?

A. Enable S3 server access logs only, and read them with Athena when needed.  
B. Configure the trail to record S3 data events (write) for the bucket.  
C. Enable CloudTrail Insights on the trail to detect unusual S3 activity.  
D. Enable AWS Config recording for S3 so deletions are tracked as configuration changes.  

### Q35

Session items in a DynamoDB table must be deleted automatically 24 hours after creation at no extra cost.
What should be used?

A. A scheduled Lambda function that scans the table and deletes the expired items.  
B. DynamoDB Streams with a consumer that deletes items.  
C. DynamoDB Time to Live (TTL) on an expiry attribute.  
D. An S3 lifecycle rule that expires the session records.  

### Q36

IoT sensor readings arrive in Kinesis Data Streams. The company needs a 5-minute tumbling-window average per device computed in real time with stateful, exactly-once processing.
Which service should be used?

A. Amazon Managed Service for Apache Flink.  
B. Amazon Data Firehose with a 300-second buffer.  
C. A Lambda function invoked per record.  
D. A nightly AWS Glue job.  

### Q37

An application needs 200 configuration values and a few API keys stored securely and cost-effectively. None of them require automatic rotation.
Which service is the MOST cost-effective?

A. AWS Secrets Manager for every value, with rotation disabled.  
B. Amazon S3 objects encrypted with SSE-S3, read by the application at startup.  
C. A DynamoDB table with client-side encryption of each attribute.  
D. AWS Systems Manager Parameter Store, using standard parameters and SecureString for secrets.  

### Q38

A team wants to analyze AWS Glue and Lambda logs ad hoc and also retain them cheaply for long-term SQL analysis.
Which TWO actions should the team take? (Select TWO.)

A. Load logs into an Amazon EMR HBase cluster.  
B. Use CloudWatch Logs Insights for interactive queries on recent logs.  
C. Copy logs by hand into a Redshift cluster each week.  
D. Trace functions with AWS X-Ray.  
E. Use a subscription filter to stream logs through Amazon Data Firehose to S3 and query them with Athena.  

### Q39

A transformation bug loaded incorrect values into Redshift over the last 7 days. The team wants a design that allows corrected data to be reprocessed easily in the future.
Which design best supports this?

A. Rely on Firehose to retain the records for 7 days so they can be reloaded.  
B. Delete the source files after loading to reduce storage cost.  
C. Keep raw immutable data in S3 and make downstream loads idempotent (stage, then MERGE).  
D. Retain only the transformed data in Redshift to keep the design simple.  

### Q40

An Athena table is partitioned by minute and holds years of data. Queries have slow planning time and many small files are scanned.
What should the data engineer do?

A. Repartition to daily or hourly partitions and compact small files into larger Parquet files.  
B. Add more partition columns, such as second, to prune the data further.  
C. Convert the data to CSV so Athena can read it without a schema lookup.  
D. Create more Athena workgroups so the queries are planned in parallel.  

### Q41

An ALTER TABLE statement on a Redshift table hangs. A long-running open transaction from another session is suspected.
How should the data engineer investigate and resolve this?

A. Increase the WLM queue count so the ALTER TABLE statement gets a slot.  
B. Run VACUUM on the table to release any locks held on it.  
C. Resize the cluster so the blocked statement runs on more nodes.  
D. Query STV_LOCKS and SVV_TRANSACTIONS to find the blocker, then end it with PG_TERMINATE_BACKEND.  

### Q42

A pipeline calls a third-party REST API that allows about 100 requests per minute and returns HTTP 429 when exceeded. Jobs are submitted in bursts.
Which design respects the limit with the LEAST operational overhead?

A. Invoke the API from many parallel Lambda functions as fast as possible.  
B. Queue requests in SQS and process them with Lambda at low maximum concurrency, with backoff on 429s.  
C. Run the calls from a large EC2 instance and ignore the 429 responses.  
D. Run an EMR cluster that makes the calls in parallel from every node.  

### Q43

Regulation requires that data and its processing stay in eu-central-1. The security team wants to PREVENT any use of other Regions across all accounts.
Which solution meets this requirement?

A. Enable S3 Cross-Region Replication to a second Region for resilience.  
B. Apply IAM permission boundaries to every developer role in the accounts.  
C. An AWS Organizations SCP that denies actions when aws:RequestedRegion is not eu-central-1.  
D. Use AWS Config rules to detect resources created in other Regions.  

### Q44

An application stores 5 million embeddings in Amazon Aurora PostgreSQL for semantic search. It needs the best recall at low query latency, and higher memory use and index build time are acceptable.
Which index should be used on the embedding column?

A. A B-tree index on the embedding column.  
B. A GIN index with a full-text search configuration.  
C. An IVFFlat index built with a list count suited to the data size.  
D. An HNSW index with pgvector.  
