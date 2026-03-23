"""
Tech Life Bingo questions — coding habits, IDE preferences, and developer culture.

24 squares (+ 1 FREE center) for a 5x5 board.
"""

from typing import Final

# ── Easy ────────────────────────────────────────────────────────────────────
# ~40-50% of squares so every comfort level can participate
# ── Medium ──────────────────────────────────────────────────────────────────
# Everyday dev situations that spark stories
# ── Bold / Wildcards ─────────────────────────────────────────────────────────
# Playful action-based prompts

TECH_LIFE_QUESTIONS: Final[list[str]] = [
    # Easy
    "Uses dark mode",
    "Has copy-pasted code from Stack Overflow",
    "Prefers VS Code",
    "Uses print() for debugging",
    "Drinks coffee (or tea) while coding",
    "Has 10+ browser tabs open right now",
    "Uses Git every day",
    "Has Googled a basic syntax question today",
    "Uses keyboard shortcuts constantly",
    "Has a to-do list that never shrinks",
    # Medium
    "Has written code past midnight",
    "Has a dotfiles repo",
    "Uses vim keybindings (in any editor)",
    "Has done a code review today",
    "Has written tests before the code (TDD)",
    "Has a strong tabs-vs-spaces opinion",
    "Has pair programmed this week",
    "Uses a linter in every project",
    "Has pushed directly to main at least once",
    # Bold / Wildcards
    'Has committed a message that says "fix" or "wip"',
    "Debugged 2+ hours only to find a typo",
    'Has a side project that\'s been "almost done" for months',
    "Teach someone a keyboard shortcut in 10 seconds → win this square",
    "Beat a teammate at rock-paper-scissors → win this square",
]
