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

    activity.main()
    updated = profile_readme.read_text(encoding="utf-8")

    assert "**Last portfolio cycle:** Cycle 91, completed on 2026-04-10" in updated
    assert "**Current focus:** `cloud-posture-watch`" in updated
    assert "- Added watch-mode state persistence" in updated
    assert "**Current publish blocker**" in updated
    assert "Target and central pushes are DNS-blocked." in updated
