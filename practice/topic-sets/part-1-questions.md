# Topic Set — Part 1 (Questions 1–24)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q1

A partner's database accepts connections only from allow-listed public IP addresses. An AWS Glue job running in a private subnet must connect to it, and the company must give the partner a stable IP address.
What should the data engineer configure?

A. An S3 gateway endpoint added to the route table of the private subnet.  
B. A NAT gateway with an Elastic IP in a public subnet; give the partner that IP.  
C. An interface VPC endpoint for AWS Glue so that the connection stays on the AWS network.  
D. A Route 53 private hosted zone that resolves the partner's database name to a fixed address.  

### Q2

A stream of payment events may contain duplicates arriving up to 10 minutes apart. The pipeline must discard duplicates in real time.
Which characteristic does the processing require?

A. Stateless processing, because each payment event can be handled independently of the others.  
B. Batch processing once per day, comparing the full day's events for duplicates.  
C. Encryption in transit between the producers and the stream, which removes replayed events.  
D. Stateful processing that remembers recently seen event IDs, such as Apache Flink with keyed state.  

### Q3

A company collects JSON clickstreams, CSV exports, PDF documents, and images. The schemas vary and change often. Which approach handles this variety MOST flexibly?

A. Land raw data in S3, apply schema-on-read through the Glue Data Catalog, and use DynamicFrames.  
B. Force every source into one relational schema before ingestion so that all data is uniform.  
C. Store every file and event as an item in a single DynamoDB table with a generic key.  
D. Reject any file that does not match a fixed schema and ask the producer to resend it.  

### Q4

When a Step Functions workflow fails, an on-call team must receive both an email and an SMS.
What is the simplest approach?

A. Write each failure to a DynamoDB table and have the on-call team query it.  
B. Poll the CloudWatch Logs group by hand and forward the error lines.  
C. Publish to an Amazon SNS topic that has both email and SMS subscriptions.  
D. Send a message to an SQS queue that the on-call team monitors.  

### Q5

An AWS DMS full load of a 3 TB database with several very large tables is taking too long. Which setting change helps MOST?

A. Use table mappings with parallel load for large tables and raise the parallel table count.  
B. Switch the replication instance to a smaller class so that fewer tasks compete for resources.  
C. Disable CDC once the load is finished so that the full load can use the whole instance.  
D. Load the tables in alphabetical order so that the large ones start last.  

### Q6

Each night a Glue crawler must finish before a Glue ETL job starts, and both should be scheduled together with minimal setup, inside Glue.
What should be used?

A. Two independent schedules set 30 minutes apart, assuming the crawler finishes first.  
B. A Glue workflow with a scheduled start trigger and a conditional trigger on crawler success.  
C. A Lambda function that sleeps until the crawler has had time to complete.  
D. An S3 lifecycle rule that moves the crawled files to the job's input prefix.  

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

A. Increase the number of workers so that more tasks write to the prefix in parallel.  
B. Disable S3 encryption on the bucket to remove the KMS request overhead.  
C. Move the bucket to another Region that has higher request rate limits.  
D. Write to more prefixes (partition the output), reduce small files, and retry with backoff.  

### Q9

A mobile app needs millisecond key lookups of device profiles at high request volume through a REST API, with no servers to manage.
Which architecture is BEST?

A. API Gateway with an EC2 fleet that reads profiles from an RDS database.  
B. API Gateway with a Lambda function that reads profiles from Amazon DynamoDB.  
C. An Athena query for every request, reading profiles from S3.  
D. A Redshift query for every request, reading profiles from a table.  

### Q10

A Step Functions task that calls a flaky API occasionally fails. The workflow should retry up to 3 times with increasing waits and then take a fallback branch.
Which feature set achieves this?

A. Retry with IntervalSeconds, BackoffRate and MaxAttempts, then a Catch that routes to a fallback state.  
B. A Parallel state that runs the task three times and keeps the first successful result.  
C. A Pass state that injects a default result when the task fails.  
D. A Wait state placed before the task so that the API has time to recover.  

### Q11

A workflow must pause until a manager approves a data load, which may take days, then continue. The solution must be serverless.
Which Step Functions capability should be used?

A. An Express workflow with a long Wait state until the approval arrives.  
B. A Map state that iterates over the pending approvals once an hour.  
C. A Standard workflow task that uses the wait-for-callback pattern with a task token.  
D. A Choice state that loops back to itself until the manager approves.  

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

A. Test only in production, where the real data volumes and permissions are available.  
B. Skip tests and rely on monitoring to catch failures after deployment.  
C. Run the full 2 TB job after every edit to confirm that the logic is correct.  
D. Factor logic into pure functions, run pytest on small samples in CI, and deploy through a pipeline.  

### Q14

A team must deploy the same Glue job, IAM role, and S3 bucket to dev, test, and prod with only parameter differences.
Which approach is BEST?

A. One CloudFormation or CDK definition that is parameterized for each environment.  
B. Manual console creation of the job, role and bucket in each account.  
C. Separate hand-written scripts for each environment, copied and edited.  
D. A spreadsheet of console steps that operators follow for every deployment.  

### Q15

A Spark join between a 2 TB table and a 50 MB lookup table creates a huge shuffle and runs slowly.
What is the BEST optimization?

A. Add more shuffle partitions only, without changing the join strategy.  
B. Broadcast the small lookup table to all executors.  
C. Convert both inputs to CSV so that Spark can split them more evenly.  
D. Run the job on a single node to avoid network shuffles.  

### Q16

The same clickstream in Kinesis Data Streams must be archived to S3 and also processed in real time by a Flink application.
What is the BEST approach?

A. Duplicate the producers so that they write to two separate streams.  
B. Export the stream to S3 in a nightly batch and run Flink on the exports.  
C. Have the Flink application write its input to both S3 and Firehose.  
D. Attach a Firehose delivery stream for S3 archival and run Flink as another consumer.  

### Q17

Item-level changes in a DynamoDB table must be captured continuously and landed in S3 with the LEAST custom code.
Which design is BEST?

A. A Lambda function that scans the table every minute and writes the changes to S3.  
B. Send the table's changes to Kinesis Data Streams and deliver them to S3 with Data Firehose.  
C. Export the whole table to S3 every hour and diff the exports.  
D. Query the table's changes directly with Athena.  

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
B. Increase the fixed worker count to 100 so that every stage has spare capacity.  
C. Move the job to a Python shell job to avoid paying for Spark executors.  
D. Disable job bookmarks so that the job needs fewer workers per run.  

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

A. Increase the ETL job's workers so that the read finishes in less time.  
B. Read from a read replica, or export a snapshot to S3 and process the export.  
C. Run the job during business hours when the database caches are warm.  
D. Disable the database's automated backups during the ETL window.  

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

A. Increase the memory to the maximum so that the archive fits in memory.  
B. Reduce the timeout so that the function fails quickly if the archive is too large.  
C. Increase the function's ephemeral storage (/tmp), which can be set up to 10,240 MB.  
D. Place the archive in an environment variable that the function reads at start.  
