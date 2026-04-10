"""Update the Cyber Port activity block in the public profile README.

This utility reads the central Cyber Port memory and status files, builds a
short English summary, and replaces only the delimited activity block in the
GitHub profile README. It does not publish, deploy, or modify the portfolio
repositories themselves.
"""

from __future__ import annotations

import re
import json
from pathlib import Path


PROFILE_README = Path(__file__).resolve().parents[1] / "README.md"
CYBER_PORT_ROOT = Path("/Users/hiagokin/k1N-Cyber-Port")
MEMORY = CYBER_PORT_ROOT / "MEMORY.md"
STATUS = CYBER_PORT_ROOT / "PORTFOLIO_STATUS.md"
STATUS_JSON = CYBER_PORT_ROOT / "portfolio-status.json"
START = "<!-- CYBER_PORT_ACTIVITY:START -->"
END = "<!-- CYBER_PORT_ACTIVITY:END -->"


def _read(path: Path) -> str:
    """Read a UTF-8 file with a clear error when it is missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return path.read_text(encoding="utf-8")


def _latest_cycle(memory_text: str) -> tuple[str, str]:
    """Extract the current cycle number and completion date."""
    match = re.search(
        r"Last completed cycle:\s+\*\*(Cycle \d+)\*\* on \*\*([^*]+)\*\*",
        memory_text,
    )
    if not match:
        return "Unknown cycle", "unknown date"
    return match.group(1), match.group(2)


def _cycle_section(memory_text: str, cycle: str) -> str:
    """Return the Markdown section for the latest cycle."""
    pattern = rf"## {re.escape(cycle)} Summary\n(?P<body>.*?)(?=\n## Cycle \d+ Summary|\Z)"
    match = re.search(pattern, memory_text, flags=re.DOTALL)
    return match.group("body").strip() if match else ""


def _first_value(section: str, label: str, default: str) -> str:
    """Extract the first value from a '- Label: value' line."""
    match = re.search(rf"^- {re.escape(label)}:\s*(.+)$", section, flags=re.MULTILINE)
    return match.group(1).strip() if match else default


def _bullets_after(section: str, heading: str, limit: int = 4) -> list[str]:
    """Collect the first bullets from a simple subsection."""
    marker = f"- {heading}:"
    start = section.find(marker)
    if start < 0:
        return []
    lines = section[start:].splitlines()[1:]
    bullets: list[str] = []
    for line in lines:
        if line.startswith("- ") and not line.startswith("  - "):
            break
        if line.startswith("  - "):
            bullets.append(line[4:].strip())
        if len(bullets) >= limit:
            break
    return bullets


def _read_portfolio_status_json(path: Path | None = None) -> list[dict]:
    """Load the structured portfolio status document."""
    return json.loads(_read(path or STATUS_JSON))


def _normalize_repo_name(name: str) -> str:
    """Present repo names without the internal k1n- prefix."""
    cleaned = name.strip().strip("`")
    return cleaned[4:] if cleaned.startswith("k1n-") else cleaned


def _display_target(target_value: str, next_repo: str) -> str:
    """Choose a clean public-facing focus repo from free-form target text."""
    normalized_target = _normalize_repo_name(target_value)
    if next_repo != "unknown":
        next_repo_aliases = {next_repo, f"k1n-{next_repo}"}
        if any(alias in target_value for alias in next_repo_aliases):
            return next_repo

    backticked = re.findall(r"`([^`]+)`", target_value)
    if backticked:
        return _normalize_repo_name(backticked[-1])

    repo_like = re.findall(r"\b(?:k1n-)?[a-z0-9]+(?:-[a-z0-9]+)+\b", target_value.lower())
    if repo_like:
        return _normalize_repo_name(repo_like[-1])

    return normalized_target


def _portfolio_summary_from_json(status_rows: list[dict]) -> tuple[str, str, list[str], str | None]:
    """Extract backlog, next target, visible gaps, and any active publish blocker."""
    if not status_rows:
        return "unknown", "unknown", [], None

    backlog = str(sum(int(item.get("open_roadmap_items", 0)) for item in status_rows))
    ranked = sorted(status_rows, key=lambda item: (int(item.get("priority_rank", 999)), item.get("name", "")))
    active = next((item for item in ranked if int(item.get("open_roadmap_items", 0)) > 0), ranked[0])
    repo = _normalize_repo_name(str(active.get("name", "unknown")))
    gaps = [str(item).strip() for item in active.get("open_roadmap_preview", []) if str(item).strip()][:3]
    blocker = active.get("last_central_preflight_blocker")
    return backlog, repo, gaps, str(blocker).strip() if blocker else None


def _portfolio_summary_from_markdown(status_text: str) -> tuple[str, str, list[str]]:
    """Fallback parser for the human-readable status document."""
    backlog = "unknown"
    match = re.search(r"Total open roadmap items:\s+\*\*(\d+)\*\*", status_text)
    if match:
        backlog = match.group(1)

    repo = "unknown"
    match = re.search(r"\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*(?:complete-now|complete-next|expand-then-complete)\s*\|\s*[1-9]\d*\s*\|", status_text)
    if match:
        repo = _normalize_repo_name(match.group(1))

    gaps: list[str] = []
    if repo != "unknown":
        section_match = re.search(rf"### {re.escape(repo)}\n(?P<body>.*?)(?=\n### |\Z)", status_text, re.DOTALL)
        if section_match:
            for line in section_match.group("body").splitlines():
                if line.startswith("  - "):
                    gaps.append(line[4:].strip())
                if len(gaps) >= 3:
                    break
    return backlog, repo, gaps


def build_activity_block() -> str:
    """Build the public Cyber Port activity block."""
    memory_text = _read(MEMORY)
    cycle, date = _latest_cycle(memory_text)
    section = _cycle_section(memory_text, cycle)

    raw_target = _first_value(section, "Target repository", "`cloud-posture-watch`")
    focus = _first_value(section, "Focus area", "continuous defensive portfolio improvement")
    delivered = _bullets_after(section, "Delivered", limit=4)
    blocker: str | None = None

    try:
        backlog, next_repo, gaps, blocker = _portfolio_summary_from_json(_read_portfolio_status_json())
    except (FileNotFoundError, json.JSONDecodeError):
        status_text = _read(STATUS)
        backlog, next_repo, gaps = _portfolio_summary_from_markdown(status_text)
    target = _display_target(raw_target, next_repo)

    delivered_lines = "\n".join(f"- {item}" for item in delivered) or "- Latest cycle details are being synchronized."
    gap_lines = "\n".join(f"- {item}" for item in gaps) or f"- Continue completion-first work in `{next_repo}`."
    blocker_block = ""
    if blocker:
        blocker_block = f"""
**Current publish blocker**

- {blocker}
"""

    return f"""{START}
**Last portfolio cycle:** {cycle}, completed on {date}  
**Current focus:** `{target}`  
**Latest validated adjustment:** {focus}.

**What changed recently**

{delivered_lines}

**Portfolio status**

- Portfolio backlog: {backlog} open roadmap items across 13 repositories.
- Next completion-first target: `{next_repo}`.
- License baseline: CC BY 4.0 with attribution.
{blocker_block}

**Next visible focus**

{gap_lines}

**Automation policy**

Cyber Port runs as a continuous automatic improvement loop. Each cycle updates tests, documentation, portfolio memory, central index status, and this profile activity block without requiring manual launch buttons. If publishing is blocked by a Git divergence or remote issue, the automation records the blocker, avoids force-push, and continues with the next safe validation or improvement path.
{END}"""


def main() -> None:
    """Replace the activity block in the profile README."""
    readme = _read(PROFILE_README)
    block = build_activity_block()
    pattern = rf"{re.escape(START)}.*?{re.escape(END)}"
    updated, count = re.subn(pattern, block, readme, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError("Cyber Port activity block markers were not found exactly once.")
    PROFILE_README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
