# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 101, completed on 2026-04-10  
**Current focus:** `hiagokinlevi-profile`  
**Latest validated adjustment:** public activity fallback hardening for stale central next-target metadata.

**What changed recently**

- Added cycle-summary `Next target` parsing to `scripts/update_cyber_port_activity.py` so the profile activity block can trust the newest completed cycle even when central `portfolio-status.json` is stale.
- Added regression coverage proving the updater prefers the latest cycle summary over stale central next-target data.
- Re-ran `python3 /Users/hiagokin/hiagokinlevi-profile/scripts/update_cyber_port_activity.py` so the profile README can promote Cycle 101 from automation memory while the central index remains read-only.

**Portfolio status**

- Portfolio backlog: 132 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `/Users/hiagokin/k1N-Cyber-Port` remains read-only and diverged (`ahead 112, behind 7`), so conflict-free reconciliation and central status-file updates are still unsafe in this run.
- `/Users/hiagokin/cloud-posture-watch` remains read-only here, so the final GitHub Actions marketplace action cannot be implemented or published from this run.
- `/Users/hiagokin/hiagokinlevi-profile` is writable locally, but remote fetch/push remain blocked by `Could not resolve host: github.com`.


**Next visible focus**

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
- The profile activity updater can fall back to automation memory when central index sync is blocked, keeping the public latest-activity block aligned with the newest validated cycle.
- The profile activity updater only promotes a cycle after a full `## Cycle N Summary` is present, preventing partial automation writes from surfacing as completed public activity.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
