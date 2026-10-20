# Topic Set — Part 3 Answers & Explanations (Q48–70)

### Q48 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.1 · Difficulty: Medium · Type: MC
- Correct B: Sensors wait for the object, and deferrable sensors free worker slots while waiting.
- A: Wastes a worker and is brittle.
- C: Creates excessive runs.
- D: Reinvents sensors poorly.

### Q49 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.4 · Difficulty: Medium · Type: MC
- Correct D: Managed scaling adjusts cluster capacity to workload.
- A: Pays for idle nodes.
- B: Prevents accidental termination only.
- C: Does not address worker capacity.

### Q50 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.5 · Difficulty: Medium · Type: MC
- Correct A: Throttles and usage plans limit request rates per client.
- B: Worsens exposure.
- C: Does not limit traffic.
- D: Loses visibility.

### Q51 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.8 · Difficulty: Medium · Type: MC
- Correct C: Event-driven Lambda reacts to each upload with no servers.
- A: Manual.
- B: Servers and polling.
- D: Not suited to file validation.

### Q52 — A, C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.9 · Difficulty: Medium · Type: MR
- Correct A and C: Scheduler supports time zones, one-time schedules, and flexible windows.
- B: That describes scheduled rules.
- D: Scheduler can invoke Lambda and many other targets.
- E: It is serverless.

### Q53 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.2 · Difficulty: Medium · Type: MC
- Correct B: Grouping with HAVING COUNT(*) > 1 lists duplicated keys.
- A: Lists all values.
- C: Removes duplicates rather than identifying them.
- D: Destructive.

### Q54 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.3 · Difficulty: Medium · Type: MC
- Correct D: Views present a filtered logical dataset with no extra copy.
- A: Duplicates data and adds a pipeline.
- B: Unrelated.
- C: Discovers schemas.

### Q55 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.7 · Difficulty: Medium · Type: MC
- Correct A: Metric filters turn matching log lines into metrics that alarms evaluate.
- B: Records API calls.
- C: Unrelated.
- D: Unrelated.

### Q56 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.6 · Difficulty: Medium · Type: MC
- Correct C: Glue installs extra Python modules specified through job parameters.
- A: Unnecessary.
- B: Capacity does not add a library.
- D: Unrelated.

### Q57 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.4.2 · Difficulty: Medium · Type: MC
- Correct D: Rulesets define checks and report pass or fail without code.
- A: Manual.
- B: Does not validate.
- C: Logs API calls.

### Q58 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.2 · Difficulty: Medium · Type: MC
- Correct B: The role's trust policy must allow Glue to assume it.
- A: S3 is not the one assuming the role.
- C: Not related.
- D: EC2 is not used by Glue jobs.

### Q59 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.4 · Difficulty: Medium · Type: MC
- Correct A: Scoped to needed actions and resources.
- B: Broader than needed.
- C: Excessive.
- D: Wrong service.

### Q60 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.6 · Difficulty: Medium · Type: MC
- Correct C: Managed services shift infrastructure and OS maintenance to AWS.
- A: On EC2, the customer is responsible.
- B: RDS hides the OS and AWS handles it.
- D: Both require patching, by different parties.

### Q61 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.1.7 · Difficulty: Hard · Type: MC
- Correct D: Domains hold governance settings, domain units organize groups, and projects are team workspaces.
- A: Buckets do not provide workspaces.
- B: Discover schemas.
- C: Content delivery.

### Q62 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.2.5 · Difficulty: Hard · Type: MC
- Correct A: ABAC scales by matching principal and resource tags.
- B: Does not scale.
- C: Violates least privilege.
- D: Insecure.

### Q63 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.3 · Difficulty: Hard · Type: MC
- Correct C: Encrypted snapshot copy needs a KMS key in the destination Region authorized through a snapshot copy grant.
- A: Violates policy.
- B: Insecure.
- D: Unrelated.

### Q64 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.3.4 · Difficulty: Medium · Type: MC
- Correct B: Client-side encryption protects data before it is sent.
- A: Encrypts after S3 receives it.
- C: Reduces protection.
- D: Insecure.

### Q65 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.4.1 · Difficulty: Medium · Type: MC
- Correct D: CloudTrail records KMS API calls and EventBridge can alert on them.
- A: Slow.
- B: Reports objects.
- C: Unrelated.

### Q66 — B

- Domain: D4 (Data Security and Governance) · Task/skill: 4.4.4 · Difficulty: Medium · Type: MC
- Correct B: Athena queries S3 logs directly and charges per scan.
- A: Fixed cost for occasional queries.
- C: Poor fit.
- D: Unnecessary management.

### Q67 — C

- Domain: D4 (Data Security and Governance) · Task/skill: 4.4.5 · Difficulty: Medium · Type: MC
- Correct C: Large volumes need distributed processing.
- A: Time and memory limits.
- B: Does not scale.
- D: A notification service.

### Q68 — B, E

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.2 · Difficulty: Medium · Type: MR
- Correct B and E: Macie discovers sensitive data in S3 and emits findings to other services.
- A: Macie reports; it does not mask.
- C: Macie targets S3.
- D: Macie targets S3.

### Q69 — A

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.5 · Difficulty: Hard · Type: MC
- Correct A: Preventive guardrails plus in-jurisdiction replication keep data and keys within approved Regions.
- B: Cost-driven placement violates residency.
- C: Moves data out of the EU.
- D: Irrelevant and insecure.

### Q70 — D

- Domain: D4 (Data Security and Governance) · Task/skill: 4.5.6 · Difficulty: Hard · Type: MC
- Correct D: Subscription approval triggers governed grants for managed assets.
- A: Bypasses governance.
- B: Insecure and ungoverned.
- C: Insecure.
