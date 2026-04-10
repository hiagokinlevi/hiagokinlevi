# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 94, completed on 2026-04-10  
**Current focus:** `cloud-posture-watch`  
**Latest validated adjustment:** offline AWS RDS encryption and public accessibility review.

**What changed recently**

- Added `analyzers.aws_rds_analyzer` to normalize approved `describe-db-instances` and optional `describe-db-clusters` JSON exports into offline DB instance and cluster evidence
- Added `k1n-posture scan-aws-rds` with severity gating, wrapped-response support, and Markdown report output for unencrypted storage, public RDS instances, and public DB subnet group placement
- Added regression coverage for loader shapes, analyzer findings, CLI gating, and installed-command smoke output; refreshed `README.md`, `ROADMAP.md`, `docs/overview.md`, and `docs/posture-methodology.md`, marking the AWS RDS roadmap item complete

**Portfolio status**

- Portfolio backlog: 135 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- Cloud-posture-watch now has the local Cycle 94 AWS RDS commit 50b6390, but git fetch origin --prune and git push origin main still fail with Could not resolve host: github.com; central k1N-Cyber-Port also remains ahead 105 and behind 7, so target and central publication stay blocked pending safe reconciliation.


**Next visible focus**

- GitHub Actions marketplace action
- Azure SQL encryption and firewall rules
- GCP Cloud SQL public IP and SSL enforcement

**Automation policy**

Cyber Port runs as a continuous automatic improvement loop. Each cycle updates tests, documentation, portfolio memory, central index status, and this profile activity block without requiring manual launch buttons. If publishing is blocked by a Git divergence or remote issue, the automation records the blocker, avoids force-push, and continues with the next safe validation or improvement path.
<!-- CYBER_PORT_ACTIVITY:END -->

## Main Repositories

| Area | Repositories |
| --- | --- |
| Threat Detection & Response | [honeypot-foundry](https://github.com/hiagokinlevi/honeypot-foundry), [dfir-attack-lab](https://github.com/hiagokinlevi/dfir-attack-lab), [ir-playbooks-automation](https://github.com/hiagokinlevi/ir-playbooks-automation) |
| Application & Web Security | [waf-defense-rulepacks](https://github.com/hiagokinlevi/waf-defense-rulepacks), [secure-pipeline-blueprints](https://github.com/hiagokinlevi/secure-pipeline-blueprints), [offensive-gvuln](https://github.com/hiagokinlevi/offensive-gvuln) |
| Cloud & Infrastructure Security | [cloud-posture-watch](https://github.com/hiagokinlevi/cloud-posture-watch), [iam-audit-lab](https://github.com/hiagokinlevi/iam-audit-lab), [container-defense-stack](https://github.com/hiagokinlevi/container-defense-stack) |
| Identity, Secrets & Monitoring | [secret-leak-sentinel](https://github.com/hiagokinlevi/secret-leak-sentinel), [phishing-surface-monitor](https://github.com/hiagokinlevi/phishing-surface-monitor) |
| AI & Cryptography Security | [ai-security-guardrails](https://github.com/hiagokinlevi/ai-security-guardrails), [cryptologik](https://github.com/hiagokinlevi/cryptologik) |

## Operating Principles

- Defensive and authorized security work only.
- Practical tools with tests, documentation, and repeatable validation.
- Continuous improvement through numbered Cyber Port cycles.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
