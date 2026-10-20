# Mock Exam 1 — Part 1 (Questions 1–22)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q1

A retail company streams about 12,000 records per second (about 18 MB/s in total) into Amazon Kinesis Data Streams. Three independent applications (fraud detection, a real-time dashboard, and an archiver) must each read the full stream with low latency and without slowing each other down. Traffic varies widely during promotions, and the team wants to avoid capacity planning.
Which solution meets these requirements with the LEAST operational overhead?

A. A provisioned stream with 18 shards; all three applications use shared-throughput GetRecords polling.  
B. A stream in on-demand capacity mode; register each application as an enhanced fan-out consumer.  
C. An Amazon Data Firehose stream with three delivery destinations.  
D. An Amazon MSK Serverless cluster with one consumer group shared by the three applications.  

### Q2

A company stores audit logs in Amazon S3. The logs are read frequently for the first 30 days, then accessed roughly once per quarter, but any read must return in milliseconds. Logs must be kept 5 years and then deleted. The company wants to minimize storage cost.
Which S3 Lifecycle configuration should be used?

A. Store in S3 Intelligent-Tiering and enable the Archive Access and Deep Archive Access tiers; expire after 5 years.  
B. Transition to S3 Glacier Flexible Retrieval after 30 days; expire after 5 years.  
C. Transition to S3 One Zone-IA after 30 days; expire after 5 years.  
D. Transition to S3 Glacier Instant Retrieval after 30 days; expire after 5 years.  

### Q3

An AWS Lambda function processes records from a Kinesis data stream. One malformed record makes the function throw an error. The same batch is retried repeatedly and processing of that shard stalls until the record expires.
What should a data engineer do to isolate the bad record and keep the shard moving?

A. Enable BisectBatchOnFunctionError, limit retry attempts, and add an on-failure destination (SQS).  
B. Double the number of shards so the failing batch is spread across more parallel readers.  
C. Increase the function timeout to 15 minutes so the batch has enough time to process the bad record.  
D. Register the function as an enhanced fan-out consumer so it receives records over a dedicated pipe.  

### Q4

An S3 bucket in account A is encrypted with SSE-KMS using a customer managed key (CMK) in account A. A bucket policy already allows an IAM role in account B to call s3:GetObject. Reads by the role fail with an AccessDenied error from AWS KMS.
Which TWO actions are required to fix this? (Select TWO.)

A. Change the bucket encryption to the AWS managed key aws/s3.  
B. Add a statement to the CMK key policy allowing the account B role to use kms:Decrypt.  
C. Create a KMS grant in account B for the S3 service principal.  
D. Attach an IAM policy to the account B role allowing kms:Decrypt on the CMK ARN.  
E. Enable automatic key rotation on the CMK.  

### Q5

An AWS Glue Spark job joins two large tables on customer_id. One customer_id accounts for about 60% of rows. A few executors run out of memory while the rest sit idle, and the job takes hours.
Which change MOST directly addresses the root cause?

A. Double the number of G.1X workers so the hot key's rows are processed on more executors.  
B. Enable job bookmarks so the job only reads data it has not processed in earlier runs.  
C. Add a random salt to the skewed key and join or aggregate in two stages.  
D. Switch the job to the Flex execution class to run on spare capacity at a lower price.  

### Q6

A pipeline must run an AWS Glue job, then an Athena query, then a Lambda function that publishes a notification. Steps need retries with backoff and failure branching. The team wants a serverless solution with the LEAST operational overhead.
Which service should orchestrate the pipeline?

A. Amazon MWAA with an Airflow DAG that uses Glue, Athena and Lambda operators.  
B. AWS Glue workflows with a scheduled start trigger, conditional triggers and a notification step.  
C. Chained Amazon EventBridge rules that fire on each service's completion event.  
D. AWS Step Functions with .sync integrations for Glue and Athena, plus Retry and Catch.  

### Q7

A Redshift cluster stores an orders fact table (about 2 billion rows) and a customers table (about 500 million rows). They are joined constantly on customer_id. Queries show large data redistribution (DS_DIST_BOTH) steps.
Which table design change will MOST improve join performance?

A. Set DISTSTYLE KEY with DISTKEY(customer_id) on both tables.  
B. Set DISTSTYLE ALL on the customers table so every node holds a full copy for local joins.  
C. Set DISTSTYLE EVEN on both tables so rows are spread evenly across all slices.  
D. Set DISTSTYLE ALL on the orders table so each node can join its own copy locally.  

### Q8

A company receives 2 TB of CSV files in S3 each day. A daily job must apply custom PySpark transformations, join the data with a reference table in an Amazon RDS for PostgreSQL database, and write partitioned Parquet files. The team does not want to manage clusters.
Which solution is MOST appropriate?

A. An AWS Lambda function with 10 GB of memory, invoked daily by an EventBridge schedule.  
B. A long-running Amazon EMR cluster on EC2 with Spark and a JDBC driver installed.  
C. An AWS Glue Spark job with a JDBC connection, started by a scheduled trigger.  
D. An Amazon Athena CTAS query that joins the S3 data with the RDS table through federation.  

### Q9

An Athena table over 10 TB of JSON logs in S3 is queried daily with filters on event_date. Query costs and runtime are high because each query scans most of the data.
Which action will reduce both cost and runtime the MOST?

A. Increase the DML query timeout so large scans have time to finish.  
B. Use CTAS to rewrite the data as Snappy-compressed Parquet partitioned by event_date.  
C. Spread the JSON files across more S3 prefixes to parallelize the scans.  
D. Enable query result reuse so that repeated queries do not rescan the data.  

### Q10

Analysts query a customers table through Amazon Athena. The table is registered in the AWS Glue Data Catalog and stored in S3. Analysts must see all columns except ssn, while the data science role must see all columns. The company wants centrally managed, auditable permissions with the LEAST operational overhead.
Which solution meets this requirement?

A. An S3 bucket policy that denies analysts access to the objects that contain the ssn values.  
B. An IAM policy for analysts that denies glue:GetTable on the customers table.  
C. A second copy of the table without ssn in another bucket, refreshed by a nightly job.  
D. Register the S3 location with Lake Formation and grant analysts SELECT on all columns except ssn.  

### Q11

A company runs Apache Kafka on premises with Kafka Streams and Kafka Connect applications. It wants to move to AWS and keep the existing producers and consumers with minimal code changes.
Which service should the company choose?

A. Amazon MSK.  
B. Amazon Kinesis Data Streams.  
C. Amazon Data Firehose.  
D. Amazon SQS.  

### Q12

An application needs two access patterns on an orders dataset in Amazon DynamoDB: (1) list all orders for a customer, newest first; (2) fetch one order by order ID. Both must be efficient and avoid scans.
Which table design satisfies both?

A. Partition key orderId with a local secondary index whose partition key is customerId.  
B. Partition key customerId, sort key orderDate, plus a global secondary index on orderId.  
C. Partition key customerId, sort key orderDate; look up orders by orderId with a filtered Scan.  
D. Partition key orderDate and sort key customerId, queried with begins_with conditions.  

### Q13

Application events arrive as JSON and must be delivered in near real time to Amazon S3 as Parquet files, with no custom code and minimal operations.
Which solution meets these requirements?

A. Kinesis Data Streams with a Lambda function that converts the records and writes Parquet to S3.  
B. An EMR cluster running Spark Structured Streaming that writes Parquet files to S3.  
C. A Glue crawler scheduled every minute that converts new JSON files to Parquet.  
D. Amazon Data Firehose with record format conversion to Parquet using a Glue table schema.  

### Q14

At the start of each business hour, many analysts open dashboards that run short queries on an Amazon Redshift provisioned cluster. Queries queue for minutes during these bursts and are fast the rest of the day.
Which approach addresses this with the LEAST effort and cost?

A. Enable concurrency scaling together with automatic workload management.  
B. Double the number of nodes permanently so the cluster can absorb the hourly peak.  
C. Convert all tables to DISTSTYLE ALL so queries do not need to redistribute rows.  
D. Move the dashboard data to Amazon RDS, which handles many concurrent short queries.  

### Q15

A nightly ETL job writes to a DynamoDB table in provisioned capacity mode. Bursts of writes from unpredictable sources cause ProvisionedThroughputExceededException. The team wants the LEAST operational overhead.
What should the data engineer do?

A. Increase the table's read capacity units to leave more headroom for the ETL job.  
B. Add DynamoDB Accelerator (DAX) in front of the table to absorb the bursts.  
C. Switch the table to on-demand capacity mode and keep retries with exponential backoff.  
D. Add a local secondary index so the ETL job can write using a different sort key.  

### Q16

A company wants to run row-level updates and deletes on data in its S3 data lake using Athena and to query the data as it looked last week. The company is evaluating Apache Iceberg tables.
Which TWO capabilities do Iceberg tables provide for this? (Select TWO.)

A. ACID row-level operations such as MERGE and DELETE.  
B. Automatic B-tree indexing of every column.  
C. Elimination of the need for any metadata or catalog.  
D. Snapshot-based time travel.  
E. Enforced foreign key constraints.  

### Q17

An AWS Glue job connects to an Amazon RDS database using a password that security policy requires to be rotated every 30 days without code changes or job downtime.
Which solution meets this requirement?

A. Store the password in a Glue job parameter and update the parameter by hand every 30 days.  
B. Store the credentials in AWS Secrets Manager with automatic rotation and reference them from the Glue connection.  
C. Store the password in an S3 object encrypted with SSE-S3 and have the job read it at start.  
D. Embed the password in the script and rotate it by redeploying the job every 30 days.  

### Q18

A partner uploads a daily file to an S3 bucket at an unpredictable time. After the file arrives, a Glue crawler and then a Glue job must run exactly once. The solution should be serverless and avoid polling.
Which design is MOST appropriate?

A. A Glue trigger that starts the crawler every hour and the job after the crawler succeeds.  
B. A Lambda function on a one-minute schedule that lists the bucket and starts the crawler.  
C. A Glue crawler scheduled to run continuously, followed by a job that starts on a timer.  
D. An S3 event to Amazon EventBridge that starts a Step Functions workflow to run the crawler and job.  

### Q19

A team wants to be alerted when a consumer application falls behind processing a Kinesis data stream.
Which approach is the MOST direct?

A. A CloudWatch alarm on WriteProvisionedThroughputExceeded, notifying an SNS topic.  
B. A CloudWatch alarm on GetRecords.IteratorAgeMilliseconds that notifies SNS.  
C. A CloudWatch alarm on IncomingBytes.  
D. A CloudTrail trail on GetRecords API calls.  

### Q20

An Amazon Redshift cluster holds 5 years of sales data. Data older than 1 year is rarely queried but must remain queryable with SQL. The company wants to cut storage cost.
Which TWO actions should be taken? (Select TWO.)

A. Add more compute nodes.  
B. Change all tables to DISTSTYLE EVEN.  
C. UNLOAD the old data to Amazon S3 in Parquet format.  
D. DELETE the old rows and run VACUUM only.  
E. Create an external schema and tables so Redshift Spectrum can query the S3 data.  

### Q21

An SQS queue triggers a Lambda function that writes to an Amazon RDS for MySQL database. During backlogs Lambda scales out and exhausts the database's connection limit.
Which change BEST protects the database?

A. Increase the function's memory so each invocation finishes faster and holds connections for less time.  
B. Set a maximum concurrency on the SQS event source mapping and use RDS Proxy for pooling.  
C. Convert the queue to a FIFO queue to preserve message ordering.  
D. Increase the queue's visibility timeout so messages are not delivered to Lambda again too early.  

### Q22

AWS Glue jobs run in a private subnet with no internet route. The jobs must read and write S3 data at the LOWEST cost.
What should be configured?

A. An S3 gateway VPC endpoint associated with the subnet's route table.  
B. A NAT gateway in a public subnet with a route from the private subnet to it.  
C. An internet gateway attached to the VPC with a default route from the private subnet.  
D. An interface VPC endpoint for AWS Glue, which provides access to the Glue APIs only.  
