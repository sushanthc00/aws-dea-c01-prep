# D. Resource Pack

> Categorized resources with exact links, timing, and when to use them.  
> ✅ = Beginner-friendly for AWS newcomers

## Official AWS Resources

### Exam Guide & Logistics
| Resource | Link | Time | When to Use | ✅ |
|---|---|---|---|---|
| Official Exam Guide (PDF) | [DEA-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf) | 30 min | Day 1 — understand scope | ✅ |
| Exam Registration | [AWS Certification](https://www.aws.training/certification) | 10 min | After you feel ready | ✅ |
| Sample Questions | [DEA-C01 Sample Questions](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Sample-Questions.pdf) | 20 min | Day 1 — calibrate difficulty | ✅ |

### AWS Skill Builder (Free Tier)
| Resource | Link | Time | When to Use | ✅ |
|---|---|---|---|---|
| Exam Prep Standard Course | [DEA-C01 Exam Prep on Skill Builder](https://explore.skillbuilder.aws/learn/course/external/view/elearning/18546/exam-prep-standard-course-aws-certified-data-engineer-associate-dea-c01) | 4-5 hrs | Days 1-3 as supplement | ✅ |
| AWS Glue Getting Started | [Glue on Skill Builder](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8171/getting-started-with-aws-glue) | 1 hr | Day 2 | ✅ |
| Data Analytics Fundamentals | [Data Analytics on Skill Builder](https://explore.skillbuilder.aws/learn/course/external/view/elearning/44/data-analytics-fundamentals) | 3.5 hrs | Optional — if you want broader context | ✅ |

### AWS Documentation (Key Pages)
| Service | Key Doc Page | Why It Matters | When to Read |
|---|---|---|---|
| S3 | [S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) | Storage class decisions are tested | Day 1 |
| Glue | [Glue Key Concepts](https://docs.aws.amazon.com/glue/latest/dg/components-key-concepts.html) | Central ETL service | Day 2 |
| Glue | [Job Bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html) | Incremental processing | Day 2 |
| Glue | [Data Quality (DQDL)](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) | Newer exam topic | Day 3 |
| Athena | [Partition Projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html) | Performance optimization | Day 3 |
| Kinesis | [Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html) | Streaming fundamentals | Day 4 |
| Kinesis | [Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) | Delivery to S3/Redshift | Day 4 |
| Redshift | [Distribution Styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html) | Performance tuning | Day 5 |
| Redshift | [COPY Command](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) | Data loading | Day 5 |
| IAM | [Policy Evaluation Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) | Security questions | Day 6 |
| KMS | [KMS Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) | Encryption questions | Day 6 |
| Lake Formation | [Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html) | Data governance | Day 7 |
| Step Functions | [Standard vs Express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) | Orchestration | Day 8 |

### AWS FAQs (High-Yield for Exam)
| Service | FAQ Link | Time | Priority |
|---|---|---|---|
| S3 | [S3 FAQ](https://aws.amazon.com/s3/faqs/) | 30 min | HIGH |
| Glue | [Glue FAQ](https://aws.amazon.com/glue/faqs/) | 20 min | HIGH |
| Kinesis | [Kinesis Streams FAQ](https://aws.amazon.com/kinesis/data-streams/faqs/) | 20 min | HIGH |
| Redshift | [Redshift FAQ](https://aws.amazon.com/redshift/faqs/) | 20 min | HIGH |
| Athena | [Athena FAQ](https://aws.amazon.com/athena/faqs/) | 15 min | HIGH |
| Lake Formation | [Lake Formation FAQ](https://aws.amazon.com/lake-formation/faqs/) | 15 min | HIGH |
| EMR | [EMR FAQ](https://aws.amazon.com/emr/faqs/) | 15 min | MEDIUM |
| Step Functions | [Step Functions FAQ](https://aws.amazon.com/step-functions/faqs/) | 10 min | MEDIUM |
| Lambda | [Lambda FAQ](https://aws.amazon.com/lambda/faqs/) | 10 min | MEDIUM |
| MSK | [MSK FAQ](https://aws.amazon.com/msk/faqs/) | 10 min | MEDIUM |

### AWS Whitepapers & Prescriptive Guidance
| Resource | Link | Time | When to Use |
|---|---|---|---|
| AWS Data Analytics Lens (Well-Architected) | [Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html) | 2 hrs | Optional — Days 9-10 if time permits |
| Building Data Lakes on AWS | [Data Lakes Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lakes-on-aws.html) | 1 hr | Optional — Day 7 supplement |

---

## Third-Party Resources (Clearly Labeled)

### Video Courses (Udemy — Free with Your Subscription)
| Resource | Link | Time | Why It Matters | When to Use |
|---|---|---|---|---|
| **Stephane Maarek — DEA-C01** (Third-party) | [Udemy Course](https://www.udemy.com/course/aws-data-engineer/) | ~15 hrs | Best structured video course for this exam | Days 1-10, primary resource |
| **Tutorials Dojo — Practice Exams** (Third-party) | [Udemy Practice Exams](https://www.udemy.com/course/aws-certified-data-engineer-associate-practice-exams/) | ~8 hrs | Most realistic practice questions | Days 11-13 |

### YouTube (Free)
| Resource | Link | Time | Why It Matters |
|---|---|---|---|
| AWS re:Invent — Building Data Lakes | Search "AWS re:Invent data lake" on YouTube | 45 min each | Real-world architecture patterns |
| AWS re:Invent — Kinesis Deep Dive | Search "AWS re:Invent Kinesis" on YouTube | 45 min | Streaming patterns |
| AWS Online Tech Talks | [AWS Online Tech Talks](https://www.youtube.com/@AWSOnlineTechTalks) | Varies | Service deep dives |

### Blogs & Community (Free)
| Resource | Link | Why It Matters |
|---|---|---|
| Tutorials Dojo Study Guide (Third-party) | [Tutorials Dojo DEA-C01 Guide](https://tutorialsdojo.com/aws-certified-data-engineer-associate/) | Excellent cheat sheets per service |
| AWS Data Engineering Blog | [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/) | Real-world patterns and solutions |

---

## Resource Usage Timeline

| Day | Primary Resource | Supplementary |
|---|---|---|
| 1 | Exam guide + Maarek S3 | S3 FAQ |
| 2 | Maarek Glue Part 1 | Glue docs |
| 3 | Maarek Glue Part 2 + Athena | Athena FAQ |
| 4 | Maarek Kinesis + MSK | Kinesis FAQ |
| 5 | Maarek Redshift | Redshift FAQ |
| 6 | Maarek Security | IAM docs |
| 7 | Maarek Lake Formation | Lake Formation FAQ |
| 8 | Maarek EMR + Step Functions | Step Functions FAQ |
| 9 | Maarek Operations | CloudWatch docs |
| 10 | Gap review + Service primer | Cheat sheet |
| 11 | Mock Exam 1 | Weakness diagnosis |
| 12 | Tutorials Dojo Exam 1 | Targeted review |
| 13 | Tutorials Dojo Exams 2-3 | Checklist review |
| 14 | Final review + rest | Exam strategy |
