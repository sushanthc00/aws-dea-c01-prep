# Mock Exam 2 — Part 2 (Questions 23–44)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q23

Financial transactions must be processed in order per account and exactly once at the application level. Volume is about 2,000 messages per second across many accounts. The team wants a managed queue.
Which design is BEST?

A. An SQS standard queue.  
B. An SQS FIFO queue using the account ID as MessageGroupId (with batching or high-throughput mode).  
C. An SNS standard topic.  
D. A single-shard Kinesis stream with random partition keys.  

### Q24

A Redshift cluster must join a local customer dimension table with 200 TB of cold Parquet data in S3 without loading the S3 data.
What should be used?

A. COPY into the cluster.  
B. Federated query.  
C. Redshift Spectrum external tables registered in the Glue Data Catalog.  
D. DMS.  

### Q25

A Glue crawler pointed at a prefix containing files with two different schemas produces a single table with confusing columns.
What is the BEST remedy?

A. Run the crawler more often.  
B. Increase the crawler's DPUs.  
C. Disable classifiers.  
D. Store different schemas under separate prefixes (or use exclusion patterns) so each is crawled into its own table.  

### Q26

Policy requires that the symmetric customer managed KMS key used by several services be rotated annually without changing the key ID or aliases referenced by applications.
What should be done?

A. Enable automatic key rotation on the customer managed key.  
B. Create a new key every year and update every application.  
C. Switch to an AWS owned key.  
D. Delete and recreate the key.  

### Q27

An S3 event triggers a Lambda function that inserts a row into a database. S3 events and Lambda retries are at-least-once, and duplicate rows occasionally appear.
What is the BEST fix?

A. Increase Lambda memory.  
B. Switch to a larger database instance.  
C. Make the write idempotent, for example a conditional insert or upsert keyed by object key plus version/ETag.  
D. Disable retries and accept lost events.  

### Q28

A DynamoDB table has a steady, predictable load 24/7 and the team wants the lowest cost.
Which configuration is BEST?

A. On-demand capacity with no changes.  
B. Provisioned capacity set at the daily peak with no scaling.  
C. Maximum reserved capacity for ten times the load.  
D. Provisioned capacity with auto scaling, optionally with reserved capacity for the baseline.  

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

A. Share one primary workgroup.  
B. A workgroup per team with a per-query data usage limit and data usage alarms (SNS).  
C. S3 Intelligent-Tiering.  
D. Redshift WLM.  

### Q31

Before landing customer data in a curated zone, an ETL job must detect and redact email addresses and phone numbers.
Which approach is BEST?

A. Delete the columns by hand.  
B. Encrypt the whole bucket.  
C. Use AWS Glue sensitive data detection in the job to find and mask or hash the PII.  
D. Use a Macie job only.  

### Q32

An SNS topic receives orders of types retail, wholesale, and export. Each type must go only to its own SQS queue without code.
What should be configured?

A. Three separate topics created by the producer.  
B. A Lambda function to route.  
C. EventBridge Scheduler.  
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

A. Short query acceleration and automatic WLM with query priorities.  
B. DISTSTYLE ALL.  
C. More S3 prefixes.  
D. A larger Athena workgroup.  

### Q35

External partners need a serverless REST API to retrieve daily aggregated results stored in S3 and queried with Athena.
Which design is MOST appropriate?

A. Give partners direct Athena console access.  
B. Amazon API Gateway with a Lambda function that runs or reads precomputed Athena results.  
C. An EC2 web server running Spark.  
D. A public S3 bucket.  

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

A. CloudTrail Insights.  
B. AWS Config rule for S3 bucket encryption with an automatic remediation action (Systems Manager Automation).  
C. Amazon Macie.  
D. S3 Transfer Acceleration.  

### Q38

A producer calls PutRecord once per event and often receives write throttling errors, even though total throughput is below the stream's capacity.
How should the producer be improved?

A. Reduce the number of shards.  
B. Disable encryption.  
C. Send each record to a different stream.  
D. Batch records with PutRecords (or use the Kinesis Producer Library aggregation) and retry with backoff.  

### Q39

The team wants an alert before a Redshift provisioned cluster runs out of storage.
Which approach is BEST?

A. A CloudTrail trail.  
B. An AWS Config rule.  
C. A CloudWatch alarm on PercentageDiskSpaceUsed notifying an SNS topic.  
D. An S3 lifecycle rule.  

### Q40

A new optional column starts appearing in new Parquet files under an Athena table. Queries on older partitions must keep working, and the new column should be queryable.
What should the engineer do?

A. Add the column to the table definition (ALTER TABLE ADD COLUMNS or a crawler schema update); older files return NULL for it.  
B. Rewrite all historical files.  
C. Delete older partitions.  
D. Recreate the database.  

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

A. DISTSTYLE KEY.  
B. Concurrency scaling.  
C. Dynamic data masking policies attached by role.  
D. Spectrum.  

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
