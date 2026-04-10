# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 96, completed on 2026-04-10  
**Current focus:** `cloud-posture-watch`  
**Latest validated adjustment:** offline Azure SQL encryption and firewall review.

**What changed recently**

- Added `analyzers.azure_sql_analyzer` to normalize approved Azure SQL logical server and database exports, including wrapped response shapes and embedded firewall-rule evidence
- Added `k1n-posture scan-azure-sql` with severity gating and Markdown report output for disabled Transparent Data Encryption, public network access, Azure-services firewall exposure, and broad public firewall ranges
- Added regression coverage for export loading, analyzer findings, CLI gating, and installed-command smoke output; refreshed `README.md`, `ROADMAP.md`, `docs/overview.md`, and `docs/posture-methodology.md`, marking the Azure SQL roadmap item complete

**Portfolio status**

- Portfolio backlog: 134 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- Cycle 96 recorded the local cloud-posture-watch Azure SQL completion commit 2a77593, but git fetch origin --prune and git push origin main still fail with Could not resolve host: github.com; central k1N-Cyber-Port also remains ahead and behind origin, so publication stays blocked pending safe reconciliation.


**Next visible focus**

- GitHub Actions marketplace action
- GCP Cloud SQL public IP and SSL enforcement
- AWS Secrets Manager / Parameter Store vs. hardcoded credential heuristic

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
- The profile activity updater can fall back to automation memory when central index sync is blocked, keeping the public latest-activity block aligned with the newest validated cycle.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
