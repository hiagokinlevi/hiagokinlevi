from __future__ import annotations

import json

from scripts import update_cyber_port_activity as activity


def test_portfolio_summary_prefers_structured_status_json() -> None:
    rows = [
        {
            "name": "container-defense-stack",
            "priority_rank": 1,
            "open_roadmap_items": 0,
            "open_roadmap_preview": [],
        },
        {
            "name": "cloud-posture-watch",
            "priority_rank": 6,
            "open_roadmap_items": 6,
            "open_roadmap_preview": [
                "Watch mode: re-assess on a schedule and alert on new findings",
                "GitHub Actions marketplace action",
                "AWS RDS encryption and public accessibility check",
            ],
            "last_central_preflight_blocker": "Could not resolve host: github.com",
        },
        {
            "name": "secret-leak-sentinel",
            "priority_rank": 7,
            "open_roadmap_items": 16,
            "open_roadmap_preview": ["JWT token detection"],
        },
    ]

    backlog, next_repo, gaps, blocker = activity._portfolio_summary_from_json(rows)

    assert backlog == "22"
    assert next_repo == "cloud-posture-watch"
    assert gaps == [
        "Watch mode: re-assess on a schedule and alert on new findings",
        "GitHub Actions marketplace action",
        "AWS RDS encryption and public accessibility check",
    ]
    assert blocker == "Could not resolve host: github.com"


def test_build_activity_block_falls_back_to_markdown_when_json_missing(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    status_md = tmp_path / "PORTFOLIO_STATUS.md"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 90** on **2026-04-10**\n\n"
        "## Cycle 90 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: stable posture-report JSON schema for downstream tooling integration\n"
        "- Delivered:\n"
        "  - Added `k1n-posture json-schema`\n",
        encoding="utf-8",
    )
    status_md.write_text(
        "# Portfolio Status\n\n"
        "## Summary\n\n"
        "- Total open roadmap items: **137**\n\n"
        "## Completion-First Order\n\n"
        "| Priority | Repository | Track | Open Roadmap Items |\n"
        "|----------|------------|-------|--------------------|\n"
        "| 1 | container-defense-stack | beyond-ready | 0 |\n"
        "| 6 | cloud-posture-watch | complete-now | 6 |\n\n"
        "## Priority Backlog\n\n"
        "### cloud-posture-watch\n\n"
        "- Next visible roadmap gaps:\n"
        "  - Watch mode: re-assess on a schedule and alert on new findings\n"
        "  - GitHub Actions marketplace action\n"
        "  - AWS RDS encryption and public accessibility check\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "STATUS", status_md)
    monkeypatch.setattr(activity, "STATUS_JSON", tmp_path / "missing.json")
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", tmp_path / "missing-automation-memory.md")

    block = activity.build_activity_block()

    assert "**Current focus:** `cloud-posture-watch`" in block
    assert "Portfolio backlog: 137 open roadmap items across 13 repositories." in block
    assert "Watch mode: re-assess on a schedule and alert on new findings" in block
    assert "Current publish blocker" not in block


def test_main_updates_readme_with_blocker_from_json(monkeypatch, tmp_path) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    status_md = tmp_path / "PORTFOLIO_STATUS.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 91** on **2026-04-10**\n\n"
        "## Cycle 91 Summary\n\n"
        "- Target repository: central index fallback (`k1N-Cyber-Port`) after `k1n-cloud-posture-watch` remained the next completion-first target but stayed read-only in this sandbox\n"
        "- Focus area: watch mode scheduling and change detection\n"
        "- Delivered:\n"
        "  - Added watch-mode state persistence\n"
        "  - Added watch-mode CLI coverage\n",
        encoding="utf-8",
    )
    status_md.write_text("# Portfolio Status\n", encoding="utf-8")
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "container-defense-stack",
                    "priority_rank": 1,
                    "open_roadmap_items": 0,
                    "open_roadmap_preview": [],
                },
                {
                    "name": "cloud-posture-watch",
                    "priority_rank": 6,
                    "open_roadmap_items": 5,
                    "open_roadmap_preview": [
                        "GitHub Actions marketplace action",
                        "AWS RDS encryption and public accessibility check",
                    ],
                    "last_central_preflight_blocker": "Target and central pushes are DNS-blocked.",
                },
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "STATUS", status_md)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", tmp_path / "missing-automation-memory.md")

    activity.main()
    updated = profile_readme.read_text(encoding="utf-8")

    assert "**Last portfolio cycle:** Cycle 91, completed on 2026-04-10" in updated
    assert "**Current focus:** `cloud-posture-watch`" in updated
    assert "- Added watch-mode state persistence" in updated
    assert "**Current publish blocker**" in updated
    assert "Target and central pushes are DNS-blocked." in updated


def test_build_activity_block_prefers_newer_automation_memory(monkeypatch, tmp_path) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 94** on **2026-04-10**\n\n"
        "## Cycle 94 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: offline AWS RDS encryption and public accessibility review\n"
        "- Delivered:\n"
        "  - Added `k1n-posture scan-aws-rds`\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Automation Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 95** on **2026-04-10**\n\n"
        "## Cycle 95 Summary\n\n"
        "- Target repository: `hiagokinlevi-profile`\n"
        "- Focus area: profile activity fallback to automation memory when central sync is blocked\n"
        "- Delivered:\n"
        "  - Added automation-memory fallback selection\n"
        "  - Added regression coverage for newer automation cycles\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "cloud-posture-watch",
                    "priority_rank": 6,
                    "open_roadmap_items": 4,
                    "open_roadmap_preview": [
                        "GitHub Actions marketplace action",
                        "Azure SQL encryption and firewall rules",
                    ],
                    "last_central_preflight_blocker": "Central reconciliation is blocked by DNS and read-only worktrees.",
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "**Last portfolio cycle:** Cycle 95, completed on 2026-04-10" in block
    assert "**Current focus:** `hiagokinlevi-profile`" in block
    assert "profile activity fallback to automation memory when central sync is blocked" in block
    assert "- Added automation-memory fallback selection" in block
    assert "Next completion-first target: `cloud-posture-watch`." in block


def test_build_activity_block_ignores_incomplete_newer_automation_cycle(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 96** on **2026-04-10**\n\n"
        "## Cycle 96 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: offline Azure SQL encryption and firewall review\n"
        "- Delivered:\n"
        "  - Added `k1n-posture scan-azure-sql`\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Automation Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 97** on **2026-04-10**\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "cloud-posture-watch",
                    "priority_rank": 6,
                    "open_roadmap_items": 3,
                    "open_roadmap_preview": [
                        "GitHub Actions marketplace action",
                        "GCP Cloud SQL public IP and SSL enforcement",
                    ],
                    "last_central_preflight_blocker": "Central reconciliation remains blocked.",
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "**Last portfolio cycle:** Cycle 96, completed on 2026-04-10" in block
    assert "**Current focus:** `cloud-posture-watch`" in block
    assert "offline Azure SQL encryption and firewall review" in block
    assert "- Added `k1n-posture scan-azure-sql`" in block


def test_latest_cycle_supports_concise_automation_memory_format() -> None:
    cycle, date = activity._latest_cycle(
        "# Cyber Port Continuous Memory\n\n"
        "- Runtime: 2026-04-10T23:35:21Z\n"
        "- Completed Cycle 99 in `hiagokinlevi-profile`: hardened profile activity fallback parsing.\n"
    )

    assert cycle == "Cycle 99"
    assert date == "2026-04-10"


def test_latest_cycle_supports_completed_cycle_bullet_format() -> None:
    cycle, date = activity._latest_cycle(
        "# Cyber Port Continuous Automation Memory\n\n"
        "- Last run: 2026-04-11T00:41:35Z\n"
        "- Completed cycle: 102\n"
        "- Target repo advanced: `/Users/hiagokin/cloud-posture-watch`\n"
    )

    assert cycle == "Cycle 102"
    assert date == "2026-04-11"


def test_build_activity_block_prefers_newer_concise_automation_cycle(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 98** on **2026-04-10**\n\n"
        "## Cycle 98 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: offline GCP Cloud SQL public IP and SSL/TLS review\n"
        "- Delivered:\n"
        "  - Added `k1n-posture scan-gcp-cloud-sql`\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Continuous Memory\n\n"
        "- Runtime: 2026-04-10T23:35:21Z\n"
        "- Completed Cycle 99 in `hiagokinlevi-profile`: profile activity fallback parser hardening.\n\n"
        "## Cycle 99 Summary\n\n"
        "- Target repository: `hiagokinlevi-profile`\n"
        "- Focus area: profile activity fallback parser hardening for concise automation memory\n"
        "- Delivered:\n"
        "  - Added concise automation-memory cycle parsing\n"
        "  - Added regression coverage for concise memory selection\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "cloud-posture-watch",
                    "priority_rank": 6,
                    "open_roadmap_items": 2,
                    "open_roadmap_preview": [
                        "GitHub Actions marketplace action",
                        "AWS Secrets Manager / Parameter Store vs. hardcoded credential heuristic",
                    ],
                    "last_central_preflight_blocker": "Central reconciliation and publishing remain blocked by GitHub DNS failure.",
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "**Last portfolio cycle:** Cycle 99, completed on 2026-04-10" in block
    assert "**Current focus:** `hiagokinlevi-profile`" in block
    assert "profile activity fallback parser hardening for concise automation memory" in block
    assert "- Added concise automation-memory cycle parsing" in block


def test_build_activity_block_supports_bullet_only_automation_memory(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 101** on **2026-04-10**\n\n"
        "## Cycle 101 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: validation-blocker fallback\n"
        "- Delivered:\n"
        "  - Added missing-module detection\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Continuous Automation Memory\n\n"
        "- Last run: 2026-04-11T00:41:35Z\n"
        "- Completed cycle: 102\n"
        "- Target repo advanced: `/Users/hiagokin/cloud-posture-watch`\n"
        "- Target commit: `0db89fb` (`Add GitHub Actions marketplace entrypoint`)\n"
        "- Validation: focused action tests passed `51 passed`\n"
        "- Blockers: central remains diverged `ahead 114, behind 7`; target/profile push still blocked by DNS\n"
        "- Next target: move to `/Users/hiagokin/secret-leak-sentinel` completion-first\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "secret-leak-sentinel",
                    "priority_rank": 7,
                    "open_roadmap_items": 16,
                    "open_roadmap_preview": [
                        "Azure SAS tokens and connection strings",
                        "GCP service account JSON key detection",
                    ],
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "**Last portfolio cycle:** Cycle 102, completed on 2026-04-11" in block
    assert "**Current focus:** `cloud-posture-watch`" in block
    assert "Validated target commit `0db89fb`" in block
    assert "focused action tests passed `51 passed`" in block
    assert "central remains diverged `ahead 114, behind 7`" in block
    assert "Next completion-first target: `secret-leak-sentinel`." in block


def test_build_activity_block_prefers_cycle_blockers_over_stale_status_json(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 98** on **2026-04-10**\n\n"
        "## Cycle 98 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: offline GCP Cloud SQL public IP and SSL/TLS review\n"
        "- Delivered:\n"
        "  - Added `k1n-posture scan-gcp-cloud-sql`\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Continuous Memory\n\n"
        "- Runtime: 2026-04-10T23:35:21Z\n"
        "- Completed Cycle 99 in `hiagokinlevi-profile`: profile activity fallback parser hardening.\n\n"
        "## Cycle 99 Summary\n\n"
        "- Target repository: `hiagokinlevi-profile`\n"
        "- Focus area: profile activity fallback parser hardening for concise automation memory\n"
        "- Delivered:\n"
        "  - Added concise automation-memory cycle parsing\n"
        "- Blockers:\n"
        "  - Central and target fetch attempts are blocked by sandbox permissions opening `.git/FETCH_HEAD`.\n"
        "  - Profile fetch and push remain blocked by `Could not resolve host: github.com`.\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "cloud-posture-watch",
                    "priority_rank": 6,
                    "open_roadmap_items": 2,
                    "open_roadmap_preview": [
                        "GitHub Actions marketplace action",
                        "AWS Secrets Manager / Parameter Store vs. hardcoded credential heuristic",
                    ],
                    "last_central_preflight_blocker": "Stale blocker text from the older central index.",
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "Central and target fetch attempts are blocked by sandbox permissions" in block
    assert "Profile fetch and push remain blocked by `Could not resolve host: github.com`." in block
    assert "Stale blocker text from the older central index." not in block


def test_build_activity_block_prefers_cycle_next_target_over_stale_status_json(
    monkeypatch, tmp_path
) -> None:
    profile_readme = tmp_path / "README.md"
    memory = tmp_path / "MEMORY.md"
    automation_memory = tmp_path / "automation-memory.md"
    status_json = tmp_path / "portfolio-status.json"

    profile_readme.write_text(
        "before\n<!-- CYBER_PORT_ACTIVITY:START -->old<!-- CYBER_PORT_ACTIVITY:END -->\nafter\n",
        encoding="utf-8",
    )
    memory.write_text(
        "# Portfolio Memory\n\n"
        "## Current Status\n\n"
        "- Last completed cycle: **Cycle 100** on **2026-04-10**\n\n"
        "## Cycle 100 Summary\n\n"
        "- Target repository: `k1n-cloud-posture-watch`\n"
        "- Focus area: offline AWS managed secrets correlation and hardcoded credential hygiene\n"
        "- Delivered:\n"
        "  - Added `k1n-posture scan-aws-secrets`\n",
        encoding="utf-8",
    )
    automation_memory.write_text(
        "# Cyber Port Automation Memory\n\n"
        "- Runtime: 2026-04-10T23:55:00Z\n"
        "- Completed Cycle 101 in `hiagokinlevi-profile`: prefer next-target fallback from cycle summaries.\n\n"
        "## Cycle 101 Summary\n\n"
        "- Target repository: `hiagokinlevi-profile`\n"
        "- Focus area: keep the public activity block aligned with the latest blocked cycle state\n"
        "- Delivered:\n"
        "  - Added cycle-summary next-target fallback for the profile updater\n"
        "- Next target: keep `k1n-cloud-posture-watch` completion-first for the remaining GitHub Actions marketplace action once publication and reconciliation are available.\n",
        encoding="utf-8",
    )
    status_json.write_text(
        json.dumps(
            [
                {
                    "name": "secret-leak-sentinel",
                    "priority_rank": 7,
                    "open_roadmap_items": 16,
                    "open_roadmap_preview": [
                        "JWT token detection",
                    ],
                    "last_central_preflight_blocker": "Stale central status picked the wrong next target.",
                }
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(activity, "PROFILE_README", profile_readme)
    monkeypatch.setattr(activity, "MEMORY", memory)
    monkeypatch.setattr(activity, "AUTOMATION_MEMORY", automation_memory)
    monkeypatch.setattr(activity, "STATUS_JSON", status_json)

    block = activity.build_activity_block()

    assert "**Last portfolio cycle:** Cycle 101, completed on 2026-04-10" in block
    assert "keep the public activity block aligned with the latest blocked cycle state" in block
    assert "Next completion-first target: `cloud-posture-watch`." in block
    assert "Next completion-first target: `secret-leak-sentinel`." not in block
