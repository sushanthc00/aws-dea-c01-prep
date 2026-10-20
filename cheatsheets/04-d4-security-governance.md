# Domain 4 — Security & Governance (18 %) — one-pager
Detail in `10-lakeformation-security.md`. Task map: 4.1 authN · 4.2 authZ · 4.3 encrypt/mask · 4.4 audit logs · 4.5 privacy/governance.

| If the stem says… | Answer pattern |
|---|---|
| column/row-level access on lake/Athena/Redshift Spectrum | **Lake Formation** (data filters, LF-tags) |
| many teams, scalable permissions | **LF-tags / ABAC**, not per-table grants |
| share lake data with another account | LF cross-account grant (RAM, resource link) + KMS key policy |
| share warehouse data without copying | **Redshift data sharing** |
| rotate DB password automatically | **Secrets Manager** rotation |
| encrypt, customer controls key, audit key use | **SSE-KMS / CMK**; reduce KMS cost with **Bucket Keys** |
| encrypt across accounts | CMK + key policy for external account + IAM in caller |
| private connectivity to S3/DynamoDB | **Gateway endpoint** |
| private connectivity to Kinesis/Glue/KMS/etc. | **Interface endpoint (PrivateLink)** |
| find PII in S3 | **Macie** (+ LF tags); mask in ETL: Glue sensitive-data detection / DataBrew; in warehouse: Redshift DDM |
| who called the API | **CloudTrail** (Lake for SQL); data events for S3 object access |
| what changed in configuration / compliance | **AWS Config** |
| analyze logs ad hoc | Athena (S3 logs, CloudTrail), Logs Insights (CloudWatch), OpenSearch (search/dashboards), EMR (huge) |
| keep data in-Region | SCP region deny, no CRR/backup copy to other Regions, regional KMS keys |
| least privilege | scoped resource ARNs, conditions, Access Analyzer; permission boundaries |
| data domain/project governance | SageMaker Unified Studio domains/units/projects + SageMaker Catalog subscriptions |
| encrypt before sending | client-side encryption (“before transit”, 4.3.4) |
Key pitfalls: AWS-managed KMS keys can't be shared cross-account · `iam:PassRole` · LF doesn't apply while IAMAllowedPrincipals has access · SG is stateful; NACL stateless · SCP never grants · Firehose→Redshift needs public cluster ✓.
