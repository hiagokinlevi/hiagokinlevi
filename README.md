# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 110, completed on 2026-04-11  
**Current focus:** `secret-leak-sentinel`  
**Latest validated adjustment:** detect JWT bearer tokens that are unsigned or rely on HMAC signing, while preserving narrow false-positive control.

**What changed recently**

- Added `jwt_weak_or_unsigned` coverage to `secret-leak-sentinel`'s primary regex detector, then base64url-decodes JWT headers so only `alg: none` and `HS256` / `HS384` / `HS512` bearer tokens are emitted as findings
- Added focused regression coverage for unsigned JWTs, HMAC-signed JWTs, invalid JWT headers, RS256 exclusions, and masked excerpts, then refreshed the target README, roadmap, and detection methodology docs
- Updated the central `README.md`, `MEMORY.md`, `ROADMAP.md`, `PORTFOLIO_STATUS.md`, and `portfolio-status.json` so Cycle 110 records the new target commit, reduced roadmap count, and the next completion-first target while preserving the CC BY 4.0 baseline

**Portfolio status**

- Portfolio backlog: 130 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git push origin main` remains blocked in `k1n-secret-leak-sentinel`, `k1N-Cyber-Port`, and `/Users/hiagokin/hiagokinlevi-profile` because outbound GitHub DNS is unavailable
- `k1N-Cyber-Port` still remains locally diverged from `origin/main` (`ahead 119, behind 8`), so direct central publication is unsafe even after the new target commit
- The default-interpreter `python3 -m secret_leak_sentinel_cli list-detectors` path still lacks `python-dotenv`, so the maintained Miniconda runtime remains the trusted CLI validation baseline here


**Next visible focus**

- HashiCorp Vault tokens
- Deep git log scan (all commits in history, not just current tree)
- Blob deduplication to avoid rescanning unchanged file content

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
- The profile activity updater accepts a full `## Cycle N Summary`, concise automation-memory completion bullets, or the richer `## Latest Run` / `## What This Run Did` automation-memory sections, so the public activity block can stay current before central sync finishes.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
