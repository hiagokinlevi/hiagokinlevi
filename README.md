# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 84, completed on 2026-04-10  
**Current focus:** `k1n-cloud-posture-watch`  
**Latest validated adjustment:** offline Azure RBAC posture review for broad standing access, guest privileged principals, service-principal Owner assignments, delegation gaps, and wildcard custom roles.

**What changed recently**

- Added `analyzers.azure_rbac_analyzer` with normalized Azure role assignment and custom role definition models for Azure CLI and Resource Graph export shapes
- Added `k1n-posture scan-azure-rbac` with repeatable `--trusted-domain`, optional external-principal suppression, severity gating, and Markdown report generation
- Flagged broad subscription or management-group Owner and Contributor grants, guest or external privileged principals, service-principal Owner assignments, User Access Administrator assignments without condition evidence, and wildcard custom-role Actions/DataActions
- Added analyzer, loader, and installed-style CLI regression coverage; refreshed README, overview, and posture methodology docs; and marked the Azure RBAC roadmap item complete

**Portfolio status**

- Portfolio backlog: 140 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Next visible focus**

- Cross-cloud IAM comparison report
- Watch mode: re-assess on a schedule and alert on new findings
- Webhook output for Slack / Teams notifications

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
