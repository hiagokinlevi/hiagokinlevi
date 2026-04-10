# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 92, completed on 2026-04-10  
**Current focus:** `cloud-posture-watch`  
**Latest validated adjustment:** scheduled watch mode for saved posture-report JSON artifacts.

**What changed recently**

- Added `reports.watch_mode` to diff current versus previous posture snapshots, track new/resolved/persistent findings, gate alerts by severity, and persist watch state between scheduled runs
- Added `k1n-posture watch-report` with `--state-file`, explicit `--previous` support, first-run suppression, and optional Slack/Teams alert delivery or dry-run payload review
- Added regression coverage for diff classification, first-run alert gating, state-file updates, and CLI dry-run output; refreshed `README.md`, `ROADMAP.md`, `docs/overview.md`, and `docs/posture-methodology.md`, marking the watch-mode roadmap item complete

**Portfolio status**

- Portfolio backlog: 136 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- The target, central index, and profile repositories all still fail git fetch origin --prune with Could not resolve host: github.com, so the Cycle 92 watch-mode change and central/profile sync commits remain local and awaiting publication.


**Next visible focus**

- GitHub Actions marketplace action
- AWS RDS encryption and public accessibility check
- Azure SQL encryption and firewall rules

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
