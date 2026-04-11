# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 102, completed on 2026-04-10  
**Current focus:** `cloud-posture-watch`  
**Latest validated adjustment:** Marketplace-ready GitHub Actions execution for scheduled posture workflows.

**What changed recently**

- Added a composite [`action.yml`](action.yml) for `cloud-posture-watch` that sets up Python, installs the package from the action path, validates dedicated provider/output inputs, and publishes resolved command plus latest Markdown/JSON/HTML report paths as GitHub Action outputs
- Added `scripts/github_action_entrypoint.py` with shell-free subcommand validation, workspace-relative path resolution, report discovery, and explicit blocking of `--provider` / `--output-dir` in free-form action args; added regression coverage in `tests/test_github_action_entrypoint.py`
- Refreshed `cloud-posture-watch` docs and roadmap to mark the GitHub Actions marketplace action complete; updated the central `README.md`, `ROADMAP.md`, `PORTFOLIO_STATUS.md`, and `portfolio-status.json` so Cycle 102 records the completed target and rotates the next completion-first target to `k1n-secret-leak-sentinel`

**Portfolio status**

- Portfolio backlog: 131 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git push origin main` remains blocked in `k1n-cloud-posture-watch`, `k1N-Cyber-Port`, and `/Users/hiagokin/hiagokinlevi-profile` because outbound GitHub DNS is unavailable
- Central reconciliation remains unsafe while `k1N-Cyber-Port` is still `ahead 112, behind 7`
- The central preflight still reports `cloud-posture-watch` validation blocked on missing `yaml` under the default interpreter even though the Miniconda full-suite baseline is green; and several non-target repositories plus the profile repo currently have generated `__pycache__` or `.coverage` artifacts that keep them out of publish-ready status


**Next visible focus**

- Azure SAS tokens and connection strings
- GCP service account JSON key detection
- JWT token detection (unsigned or weak-signature JWTs)

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
- The profile activity updater accepts either a full `## Cycle N Summary` or the concise automation-memory completion bullets, so the public activity block can stay current before central sync finishes.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
