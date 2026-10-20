# I. Final Exam Strategy — Tactical Guide

## Time Management

- **Total time**: 130 minutes for 65 questions (50 scored + 15 unscored)
- **Target pace**: ~2 minutes per question
- **First pass**: Answer all questions you're confident about (aim for 50 min)
- **Second pass**: Return to flagged questions (aim for 35 min)
- **Final review**: Check flagged and uncertain answers (remaining time)
- **Never leave a question blank** — no penalty for guessing

### Time Checkpoints
| Questions Completed | Time Elapsed | Status |
|---|---|---|
| 16 | 30 min | On track |
| 32 | 60 min | On track |
| 48 | 90 min | On track |
| 65 (all) | 120 min | 10 min for review |

## How to Approach Scenario Questions

### The RECK Framework
1. **R**ead the last sentence first — it tells you what they're asking
2. **E**xtract requirements from the scenario (latency, cost, scale, overhead, security)
3. **C**ompare options against requirements — eliminate mismatches
4. **K**ey differentiator — find the one requirement that distinguishes the correct answer

### Common Requirement Keywords and What They Mean

| Keyword | Usually Points To |
|---|---|
| "Minimal operational overhead" | Serverless (Glue, Athena, Firehose, Lambda, Redshift Serverless) |
| "Most cost-effective" | Right-sized service, serverless, or reserved capacity |
| "Real-time" | Kinesis Data Streams, Kinesis Data Analytics, MSK |
| "Near real-time" | Kinesis Data Firehose (has buffering delay) |
| "Least amount of development effort" | Managed service, no custom code |
| "Minimize data scanned" | Parquet/ORC + partitioning |
| "Audit trail" | CloudTrail (API calls) or SSE-KMS (key usage) |
| "Cross-account" | IAM roles + trust policies, or Lake Formation sharing |
| "Fine-grained access control" | Lake Formation data filters |
| "Schema evolution" | Avro, Glue Schema Registry, Apache Iceberg |
| "Exactly-once processing" | Idempotent consumers, Flink checkpointing |
| "Compliance" | CloudTrail + S3 Object Lock, encryption, Lake Formation |

## How to Handle Ambiguous Options

1. **Both A and B seem correct?** Look for the one that better matches ALL requirements
2. **"All of the above" option?** Only choose it if every other option is independently valid
3. **Two options are very similar?** The difference is usually in one specific detail — find it
4. **You're torn between two?** Go with the AWS-native, managed, serverless option

## Elimination Techniques

### Instant Eliminators
- Any option suggesting **public access** for sensitive data → eliminate
- Any option using **IAM access keys** when roles are available → eliminate
- Any option suggesting **EC2** when a serverless option exists (and question says "minimal overhead") → eliminate
- Any option suggesting **INSERT** for bulk Redshift loading → eliminate (COPY is always better)
- Any option suggesting **Lambda** for processing > 15 min or > 10 GB → eliminate

### Service Mismatch Eliminators
- **Firehose** for real-time processing → eliminate (it's near real-time)
- **Athena** for high-concurrency BI → eliminate (use Redshift)
- **DynamoDB** for complex analytics → eliminate (use Redshift/Athena)
- **Glue Python Shell** for large data → eliminate (use Spark)
- **EMR** when question says "serverless" → eliminate (unless EMR Serverless is an option)

## Common AWS Wording Traps

| Trap | Reality |
|---|---|
| "Kinesis Data Firehose provides real-time delivery" | Firehose is NEAR real-time (60+ second buffer) |
| "S3 is eventually consistent" | S3 is now strongly consistent (since Dec 2020) |
| "Glue ETL provides real-time processing" | Glue Streaming ETL is micro-batch, not true real-time |
| "Redshift Spectrum is the same as Athena" | Different services — Spectrum extends Redshift, Athena is standalone |
| "Lake Formation replaces IAM" | Lake Formation works WITH IAM, doesn't replace it entirely |
| "CloudTrail logs everything by default" | Data events must be explicitly enabled |

## What to Do If You Blank on a Service

1. **Read the question requirements carefully** — they often hint at the answer
2. **Think about the service category**: Is it storage? Compute? Streaming? Security?
3. **Use elimination**: Even if you don't know the right answer, you can often eliminate 2 wrong ones
4. **Default to the AWS-managed/serverless option** when unsure
5. **Flag and move on** — don't spend more than 3 minutes on any question

## Intelligent Guessing Strategy

When you must guess:
1. **Eliminate obviously wrong answers** (usually 1-2 can be eliminated)
2. **Prefer the most "AWS-native" answer** — AWS exams favor their managed services
3. **Prefer serverless over managed over self-managed**
4. **Prefer the answer that addresses ALL requirements**, not just some
5. **If two answers seem equally valid**, pick the simpler one
6. **For security questions**, pick the most restrictive option that still works

## Day-of Checklist

- [ ] Get 7-8 hours of sleep the night before
- [ ] Eat a good breakfast
- [ ] Arrive 15-30 minutes early (or set up your testing space for online)
- [ ] Bring valid ID (two forms for test center)
- [ ] For online proctoring: clear desk, close all apps, stable internet
- [ ] Take a deep breath before starting
- [ ] Read the first question slowly to settle in
- [ ] Use the flag feature liberally — don't get stuck
- [ ] Take a mental break at the halfway point (close eyes for 30 seconds)
- [ ] Review flagged questions before submitting
- [ ] Trust your preparation
