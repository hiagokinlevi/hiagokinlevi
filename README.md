# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 104, completed on 2026-04-10  
**Current focus:** `secret-leak-sentinel`  
**Latest validated adjustment:** cloud credential secret coverage and dependency-light suppression loading.

**What changed recently**

- Added Azure SAS URL, Azure storage connection string, and GCP service-account JSON key indicator detection to `secret-leak-sentinel`'s primary regex scanner so the shipped CLI now catches those cloud-secret shapes during normal `scan-path`, `scan-staged`, and `scan-git` workflows
- Hardened `scanners/filesystem_scanner.py` so suppression files still load in dependency-restricted environments when `PyYAML` is absent by falling back to line-based `file:` parsing; added regression coverage for the new detector patterns and real directory-scan coverage
- Refreshed target README, overview, detection methodology, roadmap, and `.gitignore`; updated the central `README.md`, `ROADMAP.md`, `PORTFOLIO_STATUS.md`, and `portfolio-status.json` so Cycle 104 records the new target commit, reduced roadmap count, and current blocker state

**Portfolio status**

- Portfolio backlog: 129 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git push origin main` remains blocked in `k1n-secret-leak-sentinel`, `k1N-Cyber-Port`, and `/Users/hiagokin/hiagokinlevi-profile` because outbound GitHub DNS is unavailable
- Central reconciliation remains unsafe while `k1N-Cyber-Port` is still `ahead 114, behind 7`
- A fresh offline system `venv` still cannot rebuild the editable install because `setuptools.build_meta` is unavailable there, even though the Miniconda install baseline is now green


**Next visible focus**

- JWT token detection (unsigned or weak-signature JWTs)
- SSH private key detection (all formats)
- HashiCorp Vault tokens

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
