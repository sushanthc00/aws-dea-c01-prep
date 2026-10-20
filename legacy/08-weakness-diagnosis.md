# G. Weakness Diagnosis Framework

## After Each Mock Exam

### Step 1: Score by Domain

| Domain | Questions | Your Correct | Your % | Target % |
|---|---|---|---|---|
| 1. Ingestion & Transformation | ~22 | ___ | ___% | 75%+ |
| 2. Data Store Management | ~17 | ___ | ___% | 75%+ |
| 3. Operations & Support | ~13 | ___ | ___% | 70%+ |
| 4. Security & Governance | ~13 | ___ | ___% | 70%+ |
| **Total** | **65** | ___ | ___% | **75%+** |

### Step 2: Identify Weak Domains

- Any domain below 60% = **Critical weakness** — needs immediate focused study
- Any domain at 60-70% = **Moderate weakness** — review key concepts
- Any domain at 70%+ = **Adequate** — light review only

### Step 3: Categorize Wrong Answers

For each wrong answer, mark the reason:

| Reason | Count | Action |
|---|---|---|
| Didn't know the service | ___ | Study the service in the primer |
| Confused two similar services | ___ | Build a comparison table |
| Missed a key detail in the question | ___ | Practice reading questions carefully |
| Knew the concept but picked wrong option | ___ | Review elimination techniques |
| Complete guess | ___ | Study the topic from scratch |

### Step 4: Build a Remediation Plan

1. List your top 5 most-missed topics
2. For each topic, spend 20-30 minutes reviewing:
   - The relevant section in `05-service-primer.md`
   - The AWS FAQ for that service
   - The Stephane Maarek course section
3. Re-answer the questions you got wrong (without looking at answers)
4. If you still get them wrong, create a flashcard

## Exam Readiness Criteria

| Metric | Not Ready | Borderline | Ready | Confident |
|---|---|---|---|---|
| Mock exam score | < 60% | 60-70% | 70-80% | 80%+ |
| Weakest domain | < 50% | 50-60% | 60-70% | 70%+ |
| "Complete guess" count | > 15 | 10-15 | 5-10 | < 5 |
| Service confusion count | > 10 | 5-10 | 2-5 | < 2 |

**Recommendation**: Book the exam when you consistently score 75%+ on practice exams with no domain below 65%.

## Common Confusion Pairs to Review

| Service A | Service B | Key Difference |
|---|---|---|
| Kinesis Data Streams | Kinesis Data Firehose | Streams = custom processing + replay; Firehose = managed delivery |
| Athena | Redshift Spectrum | Athena = standalone serverless SQL; Spectrum = extends Redshift to S3 |
| Glue ETL | EMR | Glue = serverless, simple ETL; EMR = full cluster control, multi-framework |
| Lake Formation | IAM | Lake Formation = data-level permissions; IAM = service-level permissions |
| SSE-S3 | SSE-KMS | SSE-S3 = AWS manages keys; SSE-KMS = you control keys + audit trail |
| CloudTrail | CloudWatch | CloudTrail = API audit logs; CloudWatch = metrics + operational logs |
| EventBridge | Step Functions | EventBridge = event routing; Step Functions = workflow orchestration |
| Standard workflows | Express workflows | Standard = long-running, exactly-once; Express = short, at-least-once |
| Glue Crawler | Glue ETL Job | Crawler = schema discovery; ETL Job = data transformation |
| MSK | Kinesis Streams | MSK = Kafka compatibility; Kinesis = AWS-native simplicity |
