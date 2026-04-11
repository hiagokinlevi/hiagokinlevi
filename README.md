# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My official website is [hiagokinlevi.github.io](https://hiagokinlevi.github.io/).

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Official Links

- Website: [hiagokinlevi.github.io](https://hiagokinlevi.github.io/)
- GitHub profile: [github.com/hiagokinlevi](https://github.com/hiagokinlevi)
- LinkedIn: [br.linkedin.com/in/hiagokinlevi](https://br.linkedin.com/in/hiagokinlevi)
- Portfolio index: [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port)

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 116, completed on 2026-04-11  
**Current focus:** `secret-leak-sentinel`  
**Latest validated adjustment:** close the dotenv severity-escalation roadmap item without overstating placeholder environment templates.

**What changed recently**

- Hardened `classifiers/criticality_classifier.py` so live dotenv-family files such as `.env`, `.env.local`, `.env.production`, and `config.env` are treated as high-risk secret stores even when their suffix is not literally `.env`
- Explicitly excluded placeholder dotenv filenames such as `.env.example`, `.env.sample`, and `.env.template` from automatic escalation so documentation and sample templates do not get promoted to `CRITICAL` by filename alone
- Added dedicated classifier regressions for live dotenv variants, named `*.env` files, placeholder dotenv examples, and sample-context placeholders, then refreshed the target README, detection methodology, and roadmap to record the completed item

**Portfolio status**

- Portfolio backlog: 120 open roadmap items across 13 repositories.
- Next completion-first target: `secret-leak-sentinel`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- `git push origin main` remains blocked in `secret-leak-sentinel`, `k1N-Cyber-Port`, and `/Users/hiagokin/hiagokinlevi-profile` because outbound GitHub DNS is unavailable
- `k1N-Cyber-Port` remains locally diverged from `origin/main`, so direct central publication is still unsafe even after the new target commit
- The central workspace still carries unrelated local `CODE_OF_CONDUCT.md` and `SECURITY.md` edits that should stay out of this cycle's index commit


**Next visible focus**

- VS Code extension (calls CLI and surfaces findings inline)
- ML-based classifier to reduce false positive rate on entropy findings
- Context-aware analysis (is the file a test fixture? a documentation example?)

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
