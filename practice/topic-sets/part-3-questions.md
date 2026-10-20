# Topic Set — Part 3 (Questions 48–70)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q48

An Airflow DAG on MWAA must wait for a partner's file to appear in S3 before starting downstream tasks, without holding a worker slot during the wait.
What is the BEST approach?

A. Sleep in a Python task for 24 hours and then check for the file.  
B. Use an S3 key sensor, preferably in deferrable mode, as the first task.  
C. Run the DAG every second so that the file is detected quickly.  
D. Poll with a Lambda function that is invoked from inside the DAG body.  

### Q49

An EMR cluster's workload varies throughout the day, leaving nodes idle at night and starving jobs at peak.
Which feature should be enabled?

A. A fixed cluster size that is provisioned for the daily peak.  
B. Termination protection, which keeps nodes running until jobs finish.  
C. A larger primary node that can schedule more work during peaks.  
D. EMR managed scaling, or auto scaling policies on the instance groups.  

### Q50

A public data API backed by Lambda is occasionally overwhelmed by a few clients.
How can the engineer protect the backend?

A. Configure API Gateway throttling and usage plans with API keys.  
B. Remove authentication so that the clients' requests are not retried.  
C. Increase the Lambda timeout so that slow requests complete.  
D. Disable logging to reduce the overhead of each request.  

### Q51

Every file uploaded to a landing bucket must be validated for format, and invalid files moved to a quarantine prefix automatically.
Which solution is BEST?

A. A daily manual review of the landing bucket by the data team.  
B. An EC2 instance that polls the bucket and moves invalid files.  
C. An S3 event notification that triggers a Lambda function to validate and move the file.  
D. A scheduled Redshift query that lists the files and flags invalid ones.  

### Q52

Which TWO capabilities does Amazon EventBridge Scheduler provide compared with scheduled EventBridge rules? (Select TWO.)

A. Native time zone support.  
B. UTC-only cron expressions.  
C. One-time schedules and flexible time windows.  
D. Inability to invoke Lambda.  
E. A requirement to run servers.  

### Q53

An analyst needs to find duplicate order_id values in an S3 table queried with Athena.
Which query is correct?

A. SELECT order_id FROM orders ORDER BY order_id ASC LIMIT 100;  
B. SELECT order_id, COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*) > 1;  
C. SELECT DISTINCT order_id, COUNT(order_id) FROM orders;  
D. SELECT order_id FROM orders WHERE order_id IS NOT NULL;  

### Q54

Analysts should query only the active customers from a large table, without copying data or exposing the other rows' logic.
What should the engineer create?

A. A second copy of the table in S3 that is refreshed every night.  
B. A DynamoDB table that stores only the active customers.  
C. A Glue crawler that creates a table from the active customers' files.  
D. A view (an Athena view or a Redshift view) that filters to active customers.  

### Q55

The team wants a CloudWatch alarm whenever a Lambda function writes more than 5 log lines containing "ERROR" in 5 minutes.
What should be configured?

A. A CloudWatch Logs metric filter on the log group, with an alarm on the metric.  
B. A CloudTrail trail that records each Lambda invocation and its result.  
C. An S3 lifecycle rule on the log bucket that counts the error lines.  
D. A scheduled Redshift query over the logs that publishes the count.  

### Q56

A Glue Python job fails with an import error for a third-party library that is not included in the Glue runtime.
What should the engineer do?

A. Rewrite the job in Scala so that the library is available in the runtime.  
B. Increase the worker type so that the library can be installed on larger nodes.  
C. Supply the library with --additional-python-modules (or an S3 wheel through --extra-py-files).  
D. Disable job bookmarks so that the job reinstalls its dependencies on each run.  

### Q57

A data quality requirement states that the email column must match a valid email pattern and contain no nulls, checked on every new file with no code.
Which approach is BEST?

A. A manual spreadsheet review of each new file by the data team.  
B. S3 Select queries that filter the invalid emails when the file is read.  
C. CloudTrail logs that show which files contained invalid emails.  
D. A Glue DataBrew data quality ruleset (or Glue Data Quality) applied to the dataset.  

### Q58

A new AWS Glue job needs an IAM role. Which trust relationship is required?

A. Trust the s3.amazonaws.com service principal, because the job reads from S3.  
B. Trust the glue.amazonaws.com service principal so that Glue can assume the role.  
C. Trust the root user of another account that owns the job's script.  
D. Trust the ec2.amazonaws.com service principal, because Glue runs on EC2.  

### Q59

A Lambda function reads from a Kinesis stream and writes logs. What permissions should its execution role have for least privilege?

A. Kinesis read actions (GetRecords, GetShardIterator, DescribeStream, ListShards) on that stream, and logs write actions.  
B. kinesis:* on all streams, plus logs:* on all log groups in the account.  
C. The AdministratorAccess managed policy, so the function can read from any service.  
D. Only s3:GetObject on the bucket that the function writes to, plus basic Lambda execution.  

### Q60

Which statement correctly contrasts a managed service such as Amazon RDS with a self-managed database on EC2?

A. AWS patches the operating system of a database that runs on EC2.  
B. The customer patches the underlying operating system of an RDS instance.  
C. RDS: AWS manages OS and infrastructure patching. EC2: the customer patches OS and database.  
D. Neither option requires patching because both are covered by AWS.  

### Q61

Two business units want separate governance boundaries and each team wants its own collaboration space with its own members, compute, and data assets inside Amazon SageMaker Unified Studio.
Which constructs should be used?

A. S3 buckets with one prefix for each business unit and team.  
B. Glue crawlers with one crawler for each team.  
C. CloudFront distributions with one distribution for each business unit.  
D. Domain units for the business units and projects for each team's workspace.  

### Q62

Hundreds of projects each have their own S3 prefix and team. The company wants one IAM policy that lets a user access only resources tagged for the same team, without writing a policy per team.
Which approach is BEST?

A. ABAC that compares aws:PrincipalTag/team with the resource tag team.  
B. One IAM policy for each team, listing the team's prefixes.  
C. Administrator access for everyone, with a naming convention for projects.  
D. A shared access key for each team that is stored in Parameter Store.  

### Q63

An encrypted Redshift cluster's snapshots must be automatically copied to another Region for disaster recovery.
What additional setup is required?

A. Disable encryption on the cluster before enabling snapshot copy.  
B. Share the snapshot publicly so that the other Region can restore it.  
C. Create a snapshot copy grant for a KMS key in the destination Region and enable cross-Region copy.  
D. Use S3 Select to export the snapshot contents to the other Region.  

### Q64

Regulations require that sensitive files are never readable by AWS services even in transit staging, so the company must encrypt data before it leaves its premises.
Which approach applies?

A. Rely on S3 default encryption only, which encrypts objects after S3 receives them.  
B. Client-side encryption of the data before upload, for example with the AWS Encryption SDK.  
C. Use plain HTTP so that the data is not decrypted by an intermediate proxy.  
D. Make the bucket public so that no service needs credentials to read the data.  

### Q65

The security team wants an immediate alert when anyone disables or schedules deletion of a KMS key.
Which design is BEST?

A. A weekly manual review of the KMS console by the security team.  
B. S3 Inventory reports that list the keys that are currently disabled.  
C. An S3 lifecycle rule that deletes objects encrypted with disabled keys.  
D. An EventBridge rule on CloudTrail management events (DisableKey, ScheduleKeyDeletion) that publishes to SNS.  

### Q66

CloudTrail logs are delivered to an S3 bucket, and the team wants low-cost ad hoc SQL analysis.
What should be created?

A. A Redshift cluster that loads the logs every night with COPY.  
B. An Athena table over the CloudTrail bucket, using partition projection.  
C. A DynamoDB table that stores each log event as an item.  
D. An EMR cluster that runs continuously and parses the logs.  

### Q67

Application servers produce 50 TB of raw logs per day that must be parsed and aggregated before audit reporting.
Which approach is MOST appropriate?

A. A single Lambda function that parses each log file in turn.  
B. Manual scripts that are run on an engineer's laptop.  
C. A distributed framework such as Spark on EMR or AWS Glue, reading from S3.  
D. Amazon SNS topics that fan the log lines out to many subscribers.  

### Q68

Which TWO statements about Amazon Macie are correct? (Select TWO.)

A. It automatically masks sensitive data it finds.  
B. It discovers sensitive data in S3 using managed data identifiers.  
C. It scans Amazon Redshift tables.  
D. It scans DynamoDB tables.  
E. It publishes findings that can be sent to EventBridge and Security Hub.  

### Q69

Data of EU residents must remain within the EU, and the disaster recovery copy must also stay in an EU Region.
Which combination is BEST?

A. SCPs that deny Regions outside the approved EU Regions, replication to EU Regions only, and Region-scoped KMS keys.  
B. Cross-Region replication to whichever Region has the lowest storage cost.  
C. Replicating to a US Region for durability, with strong encryption.  
D. Making the buckets public so that the EU regulator can audit them.  

### Q70

A consumer project requests access to a published data asset in Amazon SageMaker Catalog. How is access normally granted for a managed asset?

A. The consumer emails the producer, who creates and sends an access key.  
B. The asset is copied to a public bucket where the consumer can read it.  
C. The consumer is given a shared administrator password for the producer's account.  
D. The owner approves the subscription and the catalog provisions the grant, for example through Lake Formation.  
