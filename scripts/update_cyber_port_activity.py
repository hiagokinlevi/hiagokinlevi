"""Atualiza o bloco de atividade do Cyber Port no README do perfil.

Este utilitário lê a memória e o status do índice central do Cyber Port,
gera um resumo curto em inglês e substitui apenas o bloco delimitado no
README público do perfil GitHub. Ele não executa deploys, não altera os
repositórios do portfólio e não exige serviços externos.
"""

from __future__ import annotations

import re
from pathlib import Path


PROFILE_README = Path(__file__).resolve().parents[1] / "README.md"
CYBER_PORT_ROOT = Path("/Users/hiagokin/k1N-Cyber-Port")
MEMORY = CYBER_PORT_ROOT / "MEMORY.md"
STATUS = CYBER_PORT_ROOT / "PORTFOLIO_STATUS.md"
START = "<!-- CYBER_PORT_ACTIVITY:START -->"
END = "<!-- CYBER_PORT_ACTIVITY:END -->"


def _read(path: Path) -> str:
    """Lê um arquivo UTF-8 e falha com uma mensagem clara se ele não existir."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return path.read_text(encoding="utf-8")


def _latest_cycle(memory_text: str) -> tuple[str, str]:
    """Extrai o ciclo e a data atuais da seção de status da memória."""
    match = re.search(
        r"Last completed cycle:\s+\*\*(Cycle \d+)\*\* on \*\*([^*]+)\*\*",
        memory_text,
    )
    if not match:
        return "Unknown cycle", "unknown date"
    return match.group(1), match.group(2)


def _cycle_section(memory_text: str, cycle: str) -> str:
    """Retorna a seção Markdown do ciclo mais recente."""
    pattern = rf"## {re.escape(cycle)} Summary\n(?P<body>.*?)(?=\n## Cycle \d+ Summary|\Z)"
    match = re.search(pattern, memory_text, flags=re.DOTALL)
    return match.group("body").strip() if match else ""


def _first_value(section: str, label: str, default: str) -> str:
    """Extrai o primeiro valor de uma linha '- Label: value'."""
    match = re.search(rf"^- {re.escape(label)}:\s*(.+)$", section, flags=re.MULTILINE)
    return match.group(1).strip() if match else default


def _bullets_after(section: str, heading: str, limit: int = 4) -> list[str]:
    """Coleta os primeiros bullets de uma subseção simples."""
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


def _portfolio_summary(status_text: str) -> tuple[str, str, list[str]]:
    """Extrai backlog, próximo foco e primeiras lacunas visíveis do status."""
    backlog = "unknown"
    match = re.search(r"Total open roadmap items:\s+\*\*(\d+)\*\*", status_text)
    if match:
        backlog = match.group(1)

    repo = "unknown"
    match = re.search(r"\|\s*6\s*\|\s*([^|]+?)\s*\|", status_text)
    if match:
        repo = match.group(1).strip()

    gaps: list[str] = []
    section_match = re.search(r"### cloud-posture-watch\n(?P<body>.*?)(?=\n### |\Z)", status_text, re.DOTALL)
    if section_match:
        for line in section_match.group("body").splitlines():
            if line.startswith("  - "):
                gaps.append(line[4:].strip())
            if len(gaps) >= 3:
                break
    return backlog, repo, gaps


def build_activity_block() -> str:
    """Monta o bloco de novidades público do Cyber Port."""
    memory_text = _read(MEMORY)
    status_text = _read(STATUS)
    cycle, date = _latest_cycle(memory_text)
    section = _cycle_section(memory_text, cycle)

    target = _first_value(section, "Target repository", "`cloud-posture-watch`")
    focus = _first_value(section, "Focus area", "continuous defensive portfolio improvement")
    delivered = _bullets_after(section, "Delivered", limit=4)
    backlog, next_repo, gaps = _portfolio_summary(status_text)

    delivered_lines = "\n".join(f"- {item}" for item in delivered) or "- Latest cycle details are being synchronized."
    gap_lines = "\n".join(f"- {item}" for item in gaps) or f"- Continue completion-first work in `{next_repo}`."

    return f"""{START}
**Last portfolio cycle:** {cycle}, completed on {date}  
**Current focus:** {target}  
**Latest validated adjustment:** {focus}.

**What changed recently**

{delivered_lines}

**Portfolio status**

- Portfolio backlog: {backlog} open roadmap items across 13 repositories.
- Next completion-first target: `{next_repo}`.
- License baseline: CC BY 4.0 with attribution.

**Next visible focus**

{gap_lines}

**Automation policy**

Cyber Port runs as a continuous automatic improvement loop. Each cycle updates tests, documentation, portfolio memory, central index status, and this profile activity block without requiring manual launch buttons. If publishing is blocked by a Git divergence or remote issue, the automation records the blocker, avoids force-push, and continues with the next safe validation or improvement path.
{END}"""


def main() -> None:
    """Substitui o bloco de atividade no README do perfil."""
    readme = _read(PROFILE_README)
    block = build_activity_block()
    pattern = rf"{re.escape(START)}.*?{re.escape(END)}"
    updated, count = re.subn(pattern, block, readme, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError("Cyber Port activity block markers were not found exactly once.")
    PROFILE_README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
