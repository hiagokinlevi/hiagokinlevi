# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 112, completed on 2026-04-11  
**Current focus:** `secret-leak-sentinel`  
**Latest validated adjustment:** complete the git-history roadmap track with a real CLI entrypoint, accurate commit-introduction attribution, and safer live-runtime behavior.

**What changed recently**

- Added a shipped `scan-git-history` CLI command that prints commit, author, file, line, rule, and masked evidence for historical secret findings and can emit JSON for automation
- Hardened `scanners/git_history_scanner.py` so live scans walk commits in chronological order, inspect only added lines from commit patches, and skip rescanning unchanged content through blob-level and path-aware content deduplication
- Added focused regression coverage for the new CLI path, added-line diff parsing, and blob/content dedup behavior, then refreshed the target README, roadmap, and overview docs so the completed git-history capabilities and CC BY 4.0 baseline are reflected in public project text

**Portfolio status**

- Portfolio backlog: 125 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git push origin main` remains blocked in `k1n-secret-leak-sentinel`, `k1N-Cyber-Port`, and `/Users/hiagokin/hiagokinlevi-profile` because outbound GitHub DNS is unavailable
- `k1N-Cyber-Port` remains locally diverged from `origin/main`, so direct central publication is still unsafe even after the new target commit
- The maintained Miniconda runtime still lacks `GitPython`, so live `scan-git-history` execution needs that dependency restored before history scans can run end-to-end in this environment


**Next visible focus**

- VS Code extension (calls CLI and surfaces findings inline)
- Pre-push hook in addition to pre-commit
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
- The profile activity updater accepts a full `## Cycle N Summary`, concise automation-memory completion bullets, or the richer `## Latest Run` / `## What This Run Did` automation-memory sections, so the public activity block can stay current before central sync finishes.
- Public educational value without malware, exploit kits, bypass guidance, or unsafe abuse workflows.
