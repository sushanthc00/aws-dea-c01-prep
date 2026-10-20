# Topic Set — Part 3 (Questions 48–70)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q48

An Airflow DAG on MWAA must wait for a partner's file to appear in S3 before starting downstream tasks, without holding a worker slot during the wait.
What is the BEST approach?

A. Sleep in a Python task for 24 hours.  
B. Use an S3 key sensor (preferably in deferrable mode) as the first task.  
C. Run the DAG every second.  
D. Poll with a Lambda function inside the DAG body.  

### Q49

An EMR cluster's workload varies throughout the day, leaving nodes idle at night and starving jobs at peak.
Which feature should be enabled?

A. Fixed cluster size at the peak.  
B. Termination protection.  
C. A larger primary node.  
D. EMR managed scaling (or auto scaling policies).  

### Q50

A public data API backed by Lambda is occasionally overwhelmed by a few clients.
How can the engineer protect the backend?

A. Configure API Gateway throttling and usage plans with API keys.  
B. Remove authentication.  
C. Increase Lambda timeout.  
D. Disable logging.  

### Q51

Every file uploaded to a landing bucket must be validated for format, and invalid files moved to a quarantine prefix automatically.
Which solution is BEST?

A. A daily manual review.  
B. An EC2 instance polling the bucket.  
C. An S3 event notification that triggers a Lambda function to validate and move the file.  
D. A scheduled Redshift query.  

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

A. SELECT order_id FROM orders ORDER BY order_id;  
B. SELECT order_id, COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*) > 1;  
C. SELECT DISTINCT order_id FROM orders;  
D. DELETE FROM orders;  

### Q54

Analysts should query only the active customers from a large table, without copying data or exposing the other rows' logic.
What should the engineer create?

A. A second S3 copy updated nightly.  
B. A DynamoDB table.  
C. A Glue crawler.  
D. A view (Athena view in the Data Catalog or Redshift view) that filters to active customers.  

### Q55

The team wants a CloudWatch alarm whenever a Lambda function writes more than 5 log lines containing "ERROR" in 5 minutes.
What should be configured?

A. A CloudWatch Logs metric filter on the log group and an alarm on the metric.  
B. A CloudTrail trail.  
C. An S3 lifecycle rule.  
D. A Redshift query.  

### Q56

A Glue Python job fails with an import error for a third-party library that is not included in the Glue runtime.
What should the engineer do?

A. Rewrite the job in Scala.  
B. Increase the worker type.  
C. Supply the library with the --additional-python-modules job parameter (or an S3 wheel/zip via --extra-py-files).  
D. Disable job bookmarks.  

### Q57

A data quality requirement states that the email column must match a valid email pattern and contain no nulls, checked on every new file with no code.
Which approach is BEST?

A. A manual spreadsheet review.  
B. S3 Select.  
C. CloudTrail.  
D. A Glue DataBrew data quality ruleset (or Glue Data Quality) with the checks applied to the dataset.  

### Q58

A new AWS Glue job needs an IAM role. Which trust relationship is required?

A. Trust the s3.amazonaws.com service principal.  
B. Trust the glue.amazonaws.com service principal so Glue can assume the role.  
C. Trust the root user of another account.  
D. Trust ec2.amazonaws.com.  

### Q59

A Lambda function reads from a Kinesis stream and writes logs. What permissions should its execution role have for least privilege?

A. Kinesis read actions (GetRecords, GetShardIterator, DescribeStream, ListShards) on that stream and CloudWatch Logs write actions.  
B. kinesis:* on all streams.  
C. AdministratorAccess.  
D. Only s3:GetObject.  

### Q60

Which statement correctly contrasts a managed service such as Amazon RDS with a self-managed database on EC2?

A. AWS patches the operating system of a database that runs on EC2.  
B. The customer patches the underlying OS of an RDS instance.  
C. For RDS, AWS manages the underlying OS and infrastructure patching, while on EC2 the customer patches the OS and database.  
D. Neither requires patching.  

### Q61

Two business units want separate governance boundaries and each team wants its own collaboration space with its own members, compute, and data assets inside Amazon SageMaker Unified Studio.
Which constructs should be used?

A. S3 buckets only.  
B. Glue crawlers.  
C. CloudFront distributions.  
D. Domain units to organize the business units and projects for each team's workspace within the domain.  

### Q62

Hundreds of projects each have their own S3 prefix and team. The company wants one IAM policy that lets a user access only resources tagged for the same team, without writing a policy per team.
Which approach is BEST?

A. Attribute-based access control comparing aws:PrincipalTag/team with the resource tag team in policy conditions.  
B. One policy per team.  
C. Administrator access for everyone.  
D. A shared access key.  

### Q63

An encrypted Redshift cluster's snapshots must be automatically copied to another Region for disaster recovery.
What additional setup is required?

A. Disable encryption.  
B. Share the snapshot publicly.  
C. Create a snapshot copy grant for a KMS key in the destination Region and enable cross-Region snapshot copy.  
D. Use S3 Select.  

### Q64

Regulations require that sensitive files are never readable by AWS services even in transit staging, so the company must encrypt data before it leaves its premises.
Which approach applies?

A. Rely on S3 default encryption only.  
B. Client-side encryption of the data before upload (for example with an AWS Encryption SDK or KMS-generated data keys).  
C. Use HTTP instead of HTTPS.  
D. Make the bucket public.  

### Q65

The security team wants an immediate alert when anyone disables or schedules deletion of a KMS key.
Which design is BEST?

A. A weekly manual review of the console.  
B. S3 Inventory.  
C. An S3 lifecycle rule.  
D. An EventBridge rule matching CloudTrail management events (DisableKey, ScheduleKeyDeletion) that notifies an SNS topic.  

### Q66

CloudTrail logs are delivered to an S3 bucket, and the team wants low-cost ad hoc SQL analysis.
What should be created?

A. A Redshift cluster.  
B. An Athena table over the CloudTrail bucket (using partition projection) to query the logs.  
C. A DynamoDB table.  
D. An EMR cluster running continuously.  

### Q67

Application servers produce 50 TB of raw logs per day that must be parsed and aggregated before audit reporting.
Which approach is MOST appropriate?

A. A single Lambda function.  
B. Manual scripts on a laptop.  
C. A distributed processing framework such as Spark on Amazon EMR or AWS Glue reading from S3.  
D. Amazon SNS.  

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

A. SCPs that deny Regions outside the approved EU Regions, replication only to another EU Region, and Region-scoped KMS keys.  
B. Cross-Region replication to any Region with the lowest cost.  
C. Replicating to the US for durability.  
D. Making buckets public.  

### Q70

A consumer project requests access to a published data asset in Amazon SageMaker Catalog. How is access normally granted for a managed asset?

A. The consumer emails the producer for an access key.  
B. The asset is copied to a public bucket.  
C. The consumer gets a shared admin password.  
D. The data owner approves the subscription, and the catalog provisions the grant (for example through Lake Formation or Redshift permissions).  
