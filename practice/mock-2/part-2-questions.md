# Mock Exam 2 — Part 2 (Questions 23–44)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q23

Financial transactions must be processed in order per account and exactly once at the application level. Volume is about 2,000 messages per second across many accounts. The team wants a managed queue.
Which design is BEST?

A. An SQS standard queue, with the account ID stored in each message.  
B. An SQS FIFO queue that uses the account ID as MessageGroupId, with batching.  
C. An SNS standard topic with one SQS subscriber per account.  
D. A single-shard Kinesis stream with randomly generated partition keys.  

### Q24

A Redshift cluster must join a local customer dimension table with 200 TB of cold Parquet data in S3 without loading the S3 data.
What should be used?

A. COPY the 200 TB into the cluster before running the joins.  
B. Use federated query against the S3 bucket.  
C. Redshift Spectrum external tables registered in the Glue Data Catalog.  
D. Replicate the data into Redshift with DMS.  

### Q25

A Glue crawler pointed at a prefix containing files with two different schemas produces a single table with confusing columns.
What is the BEST remedy?

A. Run the crawler more often so each run sees fewer mixed files.  
B. Increase the crawler's DPUs so that it can infer schemas more accurately.  
C. Disable the classifiers so that the crawler stops inferring formats.  
D. Store the schemas under separate prefixes (or exclusion patterns), one table per prefix.  

### Q26

Policy requires that the symmetric customer managed KMS key used by several services be rotated annually without changing the key ID or aliases referenced by applications.
What should be done?

A. Enable automatic key rotation on the customer managed key.  
B. Create a new KMS key every year and update every application and alias.  
C. Switch the services to an AWS owned key that AWS rotates for them.  
D. Delete the key and recreate it with the same alias each year.  

### Q27

An S3 event triggers a Lambda function that inserts a row into a database. S3 events and Lambda retries are at-least-once, and duplicate rows occasionally appear.
What is the BEST fix?

A. Increase the Lambda memory so that the insert finishes before the retry arrives.  
B. Switch to a larger database instance so that duplicate inserts are rejected faster.  
C. Make the write idempotent: a conditional insert or upsert keyed by object key and ETag.  
D. Disable retries and accept that some events will be lost.  

### Q28

A DynamoDB table has a steady, predictable load 24/7 and the team wants the lowest cost.
Which configuration is BEST?

A. On-demand capacity with no other changes.  
B. Provisioned capacity set at the daily peak, with no auto scaling.  
C. Maximum reserved capacity, bought for ten times the current load.  
D. Provisioned capacity with auto scaling, plus reserved capacity for the baseline.  

### Q29

Changes from a DynamoDB stream must be filtered to INSERT events only, enriched through a Lambda function, and sent to a Step Functions state machine, with minimal code.
Which service is BEST?

A. Amazon EventBridge Pipes.  
B. AWS DMS.  
C. Amazon Data Firehose.  
D. AWS DataSync.  

### Q30

Multiple teams use Athena, and finance wants to cap data scanned per query and alert when a team nears its monthly spend.
What should the engineer implement?

A. Share one primary workgroup and review the query history each month.  
B. One workgroup per team with a per-query data limit and data usage alarms to SNS.  
C. Enable S3 Intelligent-Tiering on the source bucket for each team.  
D. Create Redshift WLM queues for each team's Athena queries.  

### Q31

Before landing customer data in a curated zone, an ETL job must detect and redact email addresses and phone numbers.
Which approach is BEST?

A. Delete the PII columns by hand before each load.  
B. Encrypt the whole bucket with a customer managed KMS key.  
C. Use Glue sensitive data detection in the job to find the PII and mask or hash it.  
D. Run a Macie discovery job, which masks the PII it finds.  

### Q32

An SNS topic receives orders of types retail, wholesale, and export. Each type must go only to its own SQS queue without code.
What should be configured?

A. Three separate topics, with the producer publishing to the right one by type.  
B. A Lambda function that inspects each message and forwards it to the right queue.  
C. EventBridge Scheduler rules that poll the topic for each order type.  
D. SNS subscription filter policies on a message attribute for each SQS subscription.  

### Q33

Which TWO practices improve Athena performance and cost for a large event table? (Select TWO.)

A. Partition by commonly filtered columns with moderate cardinality such as event_date.  
B. Partition by a high-cardinality column such as user_id.  
C. Store data as many tiny files.  
D. Use a columnar format (Parquet) with larger files (for example 128 MB or more).  
E. Avoid any partitions.  

### Q34

Short, interactive Redshift queries are stuck behind long-running ETL queries in the same queue.
What should the engineer enable?

A. Short query acceleration with automatic WLM and query priorities.  
B. Set DISTSTYLE ALL on the tables that the short queries use.  
C. Add more S3 prefixes so that the queries read in parallel.  
D. Move the interactive queries to a larger Athena workgroup.  

### Q35

External partners need a serverless REST API to retrieve daily aggregated results stored in S3 and queried with Athena.
Which design is MOST appropriate?

A. Give the partners read access to the Athena console and the results bucket.  
B. Amazon API Gateway with a Lambda function that runs or reads precomputed Athena results.  
C. An EC2 web server that runs Spark against the S3 data for every request.  
D. A public S3 bucket that holds the daily result files.  

### Q36

Data archived in S3 Glacier Flexible Retrieval must be restored within 24 hours at the LOWEST cost.
Which retrieval option should be used?

A. Expedited.  
B. Standard.  
C. Bulk.  
D. Instant.  

### Q37

The company must continuously detect S3 buckets without default encryption and automatically remediate them.
Which solution is BEST?

A. CloudTrail Insights to flag buckets that are created without encryption.  
B. An AWS Config rule for S3 default encryption with automatic remediation.  
C. Amazon Macie to detect and encrypt unencrypted objects.  
D. S3 Transfer Acceleration to encrypt data in transit to the buckets.  

### Q38

A producer calls PutRecord once per event and often receives write throttling errors, even though total throughput is below the stream's capacity.
How should the producer be improved?

A. Reduce the number of shards so that each shard receives more records.  
B. Disable encryption on the stream to remove the KMS overhead per request.  
C. Send each record to a different stream to spread the write load.  
D. Batch records with PutRecords (or KPL aggregation) and retry with exponential backoff.  

### Q39

The team wants an alert before a Redshift provisioned cluster runs out of storage.
Which approach is BEST?

A. A CloudTrail trail that records the cluster's API activity.  
B. An AWS Config rule that checks the cluster's storage configuration.  
C. A CloudWatch alarm on PercentageDiskSpaceUsed that notifies an SNS topic.  
D. An S3 lifecycle rule on the cluster's snapshot bucket.  

### Q40

A new optional column starts appearing in new Parquet files under an Athena table. Queries on older partitions must keep working, and the new column should be queryable.
What should the engineer do?

A. Add the column to the table definition (ALTER TABLE ADD COLUMNS); older files return NULL.  
B. Rewrite all historical files so that they include the new column.  
C. Delete the older partitions and reload them with the new schema.  
D. Recreate the database and register every partition again.  

### Q41

A team must run an existing Spark application that depends on custom JAR files and also needs Apache HBase.
Which service is BEST?

A. AWS Glue.  
B. Amazon EMR.  
C. AWS Lambda.  
D. Amazon Athena.  

### Q42

Support agents querying a Redshift table must see only the last four digits of card numbers, while the finance role sees full values.
Which Redshift feature fits BEST?

A. DISTSTYLE KEY on the card number column.  
B. Concurrency scaling for the support team's queries.  
C. Dynamic data masking policies attached to roles.  
D. Redshift Spectrum external tables with a masked copy.  

### Q43

Kinesis producers see WriteProvisionedThroughputExceeded errors on only a few shards.
Which TWO actions help? (Select TWO.)

A. Reduce the number of shards.  
B. Use a partition key with more even distribution.  
C. Turn off the producers' retry logic.  
D. Increase shards or switch the stream to on-demand mode.  
E. Disable server-side encryption.  

### Q44

An application needs a durable, Redis-compatible primary database with microsecond reads and multi-AZ durability.
Which service is BEST?

A. Amazon DynamoDB.  
B. Amazon RDS for MySQL.  
C. Amazon DocumentDB.  
D. Amazon MemoryDB.  
