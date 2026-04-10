# Hiago Kin Levi

Cyber Ops since 2007. I build defensive security tooling for incident response, DFIR, IAM, AppSec, cloud posture, detection engineering, AI security, containers, secrets, WAFs, phishing monitoring, and applied cryptography.

My current public portfolio is [Cyber Port](https://github.com/hiagokinlevi/Cyber-Port): a 13-repository defensive security ecosystem released under CC BY 4.0.

## Cyber Port Live Activity

<!-- CYBER_PORT_ACTIVITY:START -->
**Last portfolio cycle:** Cycle 98, completed on 2026-04-10  
**Current focus:** `cloud-posture-watch`  
**Latest validated adjustment:** offline GCP Cloud SQL public IP and SSL/TLS review.

**What changed recently**

- Added `analyzers.gcp_cloud_sql_analyzer` to normalize approved `gcloud sql instances list --format=json` exports, including wrapped response shapes, public IP evidence, SSL/TLS controls, and authorized-network ranges
- Added `k1n-posture scan-gcp-cloud-sql` with severity gating and Markdown report output for public IPv4 exposure, missing SSL/TLS enforcement, and broad authorized networks
- Added regression coverage for loader shapes, analyzer findings, and CLI gating; refreshed `README.md`, `ROADMAP.md`, `docs/overview.md`, and `docs/posture-methodology.md`, marking the GCP Cloud SQL roadmap item complete

**Portfolio status**

- Portfolio backlog: 133 open roadmap items across 13 repositories.
- Next completion-first target: `cloud-posture-watch`.
- License baseline: CC BY 4.0 with attribution.

**Current publish blocker**

- Cycle 98 validated the local cloud-posture-watch GCP Cloud SQL completion commit 7219580 and the target worktree is clean again, but central and target git fetch or push still fail with Could not resolve host: github.com while the central index remains diverged from origin, so publication and reconciliation remain blocked.


**Next visible focus**

- GitHub Actions marketplace action
- AWS Secrets Manager / Parameter Store vs. hardcoded credential heuristic

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
