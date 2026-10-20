# Topic Set — Part 1 (Questions 1–24)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q1

A partner's database accepts connections only from allow-listed public IP addresses. An AWS Glue job running in a private subnet must connect to it, and the company must give the partner a stable IP address.
What should the data engineer configure?

A. An S3 gateway endpoint.  
B. A NAT gateway with an Elastic IP address in a public subnet, routed from the private subnet; give the partner that Elastic IP.  
C. An interface VPC endpoint for AWS Glue.  
D. A Route 53 private hosted zone.  

### Q2

A stream of payment events may contain duplicates arriving up to 10 minutes apart. The pipeline must discard duplicates in real time.
Which characteristic does the processing require?

A. Stateless processing, because each event is independent.  
B. Batch processing once per day.  
C. Only encryption in transit.  
D. Stateful processing that remembers recently seen event IDs, such as Apache Flink with keyed state.  

### Q3

A company collects JSON clickstreams, CSV exports, PDF documents, and images. The schemas vary and change often. Which approach handles this variety MOST flexibly?

A. Land raw data in S3 and apply schema-on-read with the Glue Data Catalog and query engines, using Glue DynamicFrames for transformation.  
B. Force all data into one relational schema before ingestion.  
C. Store everything in a single DynamoDB table.  
D. Reject any file that does not match a fixed schema.  

### Q4

When a Step Functions workflow fails, an on-call team must receive both an email and an SMS.
What is the simplest approach?

A. Write failures to a DynamoDB table.  
B. Poll CloudWatch Logs by hand.  
C. Send a message to an Amazon SNS topic that has email and SMS subscriptions.  
D. Send a message to an SQS queue.  

### Q5

An AWS DMS full load of a 3 TB database with several very large tables is taking too long. Which setting change helps MOST?

A. Use table mapping with parallel load for large tables (partitioned loads) and increase the number of tables loaded in parallel.  
B. Switch the target to a smaller instance.  
C. Disable CDC after the load.  
D. Load tables in alphabetical order.  

### Q6

Each night a Glue crawler must finish before a Glue ETL job starts, and both should be scheduled together with minimal setup, inside Glue.
What should be used?

A. Two independent schedules set 30 minutes apart.  
B. A Glue workflow with a scheduled start trigger, then a conditional trigger that starts the job when the crawler succeeds.  
C. A Lambda function that sleeps.  
D. An S3 lifecycle rule.  

### Q7

A company already runs Amazon EKS for several applications. It wants to run Spark jobs on the same cluster, sharing compute to reduce cost.
Which option is BEST?

A. AWS Glue.  
B. A dedicated EMR cluster on EC2.  
C. Amazon EMR on EKS.  
D. AWS Lambda.  

### Q8

A Glue job writing hundreds of thousands of small objects to a single S3 prefix intermittently fails with HTTP 503 Slow Down errors.
What is the BEST remediation?

A. Increase the number of workers.  
B. Disable S3 encryption.  
C. Move the bucket to another Region.  
D. Write to more prefixes (for example by partitioning output), reduce the number of small files, and use retries with exponential backoff.  

### Q9

A mobile app needs millisecond key lookups of device profiles at high request volume through a REST API, with no servers to manage.
Which architecture is BEST?

A. API Gateway with an EC2 fleet and RDS.  
B. API Gateway with a Lambda function reading Amazon DynamoDB.  
C. An Athena query per request.  
D. A Redshift query per request.  

### Q10

A Step Functions task that calls a flaky API occasionally fails. The workflow should retry up to 3 times with increasing waits and then take a fallback branch.
Which feature set achieves this?

A. Retry with IntervalSeconds, BackoffRate, and MaxAttempts, followed by a Catch that routes to the fallback state.  
B. A Parallel state.  
C. A Pass state.  
D. A Wait state only.  

### Q11

A workflow must pause until a manager approves a data load, which may take days, then continue. The solution must be serverless.
Which Step Functions capability should be used?

A. An Express workflow with a long Wait.  
B. A Map state.  
C. A Standard workflow task with the wait-for-callback pattern (task token).  
D. A Choice state.  

### Q12

A Lambda function inserts records into a database and is slow and costly. Which TWO changes reduce its runtime? (Select TWO.)

A. Create a new database connection inside the handler for every record.  
B. Initialize SDK and database clients outside the handler so execution environments reuse them.  
C. Insert records one at a time.  
D. Insert records in batches.  
E. Reduce memory to the minimum.  

### Q13

A team wants to unit test PySpark transformation logic before deploying it to AWS Glue, without running full jobs for each change.
What is the BEST practice?

A. Test only in production.  
B. Skip tests and monitor failures.  
C. Run the full 2 TB job after every edit.  
D. Factor logic into pure functions, run pytest against small sample data locally or in CI (for example with the Glue Docker image), and run it in a pipeline.  

### Q14

A team must deploy the same Glue job, IAM role, and S3 bucket to dev, test, and prod with only parameter differences.
Which approach is BEST?

A. One CloudFormation or CDK definition parameterized per environment.  
B. Manual console creation in each account.  
C. Separate hand-written scripts per environment with copy/paste.  
D. A spreadsheet of steps.  

### Q15

A Spark join between a 2 TB table and a 50 MB lookup table creates a huge shuffle and runs slowly.
What is the BEST optimization?

A. Add more shuffle partitions only.  
B. Broadcast the small lookup table to all executors.  
C. Convert both to CSV.  
D. Run the job on one node.  

### Q16

The same clickstream in Kinesis Data Streams must be archived to S3 and also processed in real time by a Flink application.
What is the BEST approach?

A. Duplicate producers to write to two streams.  
B. Batch export the stream nightly.  
C. Have Flink write to S3 and Firehose both.  
D. Attach a Firehose delivery stream to the stream for S3 archival and run the Flink application as another consumer.  

### Q17

Item-level changes in a DynamoDB table must be captured continuously and landed in S3 with the LEAST custom code.
Which design is BEST?

A. A Lambda function scanning the table every minute.  
B. Send table changes to Kinesis Data Streams (the DynamoDB Kinesis destination) and deliver them to S3 with Amazon Data Firehose.  
C. Export the whole table every hour.  
D. Query the table with Athena.  

### Q18

A company must copy 5 TB nightly from an on-premises NFS server to S3 on a schedule, with integrity verification and bandwidth control.
Which service is BEST?

A. AWS Snowball Edge.  
B. AWS Transfer Family.  
C. AWS DataSync.  
D. AWS DMS.  

### Q19

A Glue Spark job runs with a fixed 50 workers, but most of its stages use few workers, so cost is high.
What should the engineer do?

A. Enable Glue auto scaling with a maximum worker count so workers are added only when needed.  
B. Increase workers to 100.  
C. Move to Python shell.  
D. Disable bookmarks.  

### Q20

A pipeline writes high-volume events row by row, expects the schema to evolve, and downstream consumers read whole records.
Which file format is MOST suitable?

A. CSV.  
B. Parquet only.  
C. Plain text.  
D. Apache Avro.  

### Q21

Which TWO situations favor Amazon MWAA over AWS Step Functions? (Select TWO.)

A. The team already has many Apache Airflow DAGs to migrate.  
B. The workflow is a short event-driven serverless chain with minimal cost at idle.  
C. The team needs Airflow's operator ecosystem and Python-defined DAGs with rich scheduling and backfills.  
D. The workflow needs per-state-transition pricing.  
E. The workflow must be fully serverless with no environment to size.  

### Q22

A nightly ETL job reads directly from a production Amazon RDS database and slows down customer-facing queries.
What is the BEST way to reduce impact?

A. Increase the ETL job's workers.  
B. Read from a read replica (or export a snapshot to S3 and process the export).  
C. Run the job during business hours.  
D. Disable the database's backups.  

### Q23

Which TWO are valid direct destinations for Amazon S3 event notifications? (Select TWO.)

A. AWS Lambda.  
B. AWS Glue job.  
C. Amazon Redshift.  
D. Amazon SQS.  
E. AWS Direct Connect.  

### Q24

A Lambda function must unzip an 8 GB archive during processing.
What should be configured?

A. Increase the memory to the maximum only.  
B. Reduce the timeout.  
C. Increase the function's ephemeral storage (/tmp) up to 10,240 MB.  
D. Place the archive in an environment variable.  
