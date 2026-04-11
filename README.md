# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 109, completed on 2026-04-11  
**Current focus:** `secret-leak-sentinel`  
**Latest validated adjustment:** skip guaranteed `FETCH_HEAD` permission failures when `--fetch` is requested from read-only repository checkouts.

**What changed recently**

- Hardened central `scripts/repository_publish_preflight.py` so it now resolves linked-worktree git metadata paths before writability checks, which keeps the preflight accurate for normal repositories and pointer-based worktrees
- Taught the fetch path to skip attempts when the resolved git metadata directory is not writable, recording `fetch-skipped-read-only-git-dir` instead of retrying a fetch that cannot create `FETCH_HEAD`
- Added focused regression coverage for linked `.git` pointer resolution, skipped-fetch blocker classification, and next-action routing, then refreshed central `README.md`, `ROADMAP.md`, `STANDARDS.md`, `PORTFOLIO_STATUS.md`, and `portfolio-status.json` so Cycle 109 records the new fallback behavior while preserving `secret-leak-sentinel` as the next real target

**Portfolio status**

- Portfolio backlog: 131 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git fetch`/`git push` against GitHub still cannot complete safely from the central index because outbound DNS remains unavailable and `k1N-Cyber-Port` is still `ahead 119, behind 8`
- `secret-leak-sentinel` and `/Users/hiagokin/hiagokinlevi-profile` remain read-only from this run, so target edits, target commits, and the required profile README activity refresh cannot be written back here
- The active target checkout is also already dirty, which keeps it out of read-only validation mode in the current sandbox


**Next visible focus**

- JWT token detection (unsigned or weak-signature JWTs)
- HashiCorp Vault tokens
- Deep git log scan (all commits in history, not just current tree)

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
