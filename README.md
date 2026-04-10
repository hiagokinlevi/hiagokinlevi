# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 88, completed on 2026-04-10  
**Current focus:** `k1n-cloud-posture-watch`  
**Latest validated adjustment:** Slack and Microsoft Teams webhook notifications for saved posture reports.

**What changed recently**

- Added `reports.webhook_notifications` to build dependency-free Slack and Teams incoming-webhook payloads from saved JSON posture reports
- Added `k1n-posture notify-webhook` with `--target slack|teams`, `--dashboard-url`, `--dry-run`, HTTPS webhook validation, timeout control, and success output that does not print the webhook secret
- Added regression coverage for Slack payload summaries, Teams MessageCard payloads, dry-run CLI output, missing-webhook validation, and secret-safe success output
- Refreshed `k1n-cloud-posture-watch` README, overview, posture methodology, and roadmap docs, marking the Slack/Teams webhook roadmap item complete

**Portfolio status**

- Portfolio backlog: 138 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Next visible focus**

- Watch mode: re-assess on a schedule and alert on new findings
- JSON output schema stable for downstream tooling integration
- GitHub Actions marketplace action

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
