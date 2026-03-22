# Soc Ops — Project Guidelines

## Before Every PR

Run all three — do not skip:

```sh
uv run ruff check .   # lint
uv run pytest         # test
uv run uvicorn app.main:app --reload --port 8000  # verify it runs
```

## Stack
Python 3.13+, FastAPI, Jinja2, HTMX · `uv` for deps · `ruff` (88-char, E/F/I/N/W) · `pytest` + `httpx`

## Architecture

| Layer | Location | Responsibility |
|---|---|---|
| Pure logic | `app/game_logic.py` | Stateless functions; no I/O |
| Session state | `app/game_service.py` | `GameSession` dataclass; in-memory store |
| HTTP layer | `app/main.py` | FastAPI routes → Jinja2 HTML responses |

## Conventions
- **HTMX fragments** — HTMX routes return components from `app/templates/components/`; full pages use top-level templates
- **Immutable models** — `BingoSquareData`/`BingoLine` are `frozen=True`; mutate via `model_copy(update={...})`
- **Pure game logic** — `game_logic.py` has no side effects; all state lives in `GameSession`
- **GameState in templates** — always pass `{"GameState": GameState}` so Jinja2 can compare enum values

## Design System

**Theme:** Dark ops / mission-brief aesthetic. Minimal, flat, no shadows, no border-radius.

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#0D0D0D` | Page background |
| `--surface` | `#161616` | Cells, cards |
| `--fg` | `#F0EDE6` | Body text (warm cream) |
| `--muted` | `#a8a8a2` | Secondary text (≥7:1 contrast) |
| `--border` | `#2a2a28` | All dividing lines |
| `--accent` | `#FF4926` | CTAs, marked squares, step numbers |
| `--font` | Instrument Sans | UI chrome, headings |
| `--font-grid` | DM Sans | Bingo board cells only |

**Rules:**
- All `border-radius` = 0 — sharp corners everywhere
- No `box-shadow` anywhere
- Marked bingo squares: `--accent` fill + `--bg` text
- Winning squares: same accent fill + `font-bold`
- Muted text must stay ≥7:1 contrast on `--bg`; use `--fg` when in doubt

**Typography scale:**
- `.text-display` (4rem / 800) — page title `SOC OPS`
- `.text-sm` + `.uppercase` + `.tracking-widest` — labels, buttons, header
- `.font-grid` (DM Sans) — board cell text for smooth legibility at small sizes

**Animations:**
- `.fade-in-1` through `.fade-in-4` — staggered entrance on start screen (90 ms apart)
- `.slide-up` — modal entrance (cubic-bezier spring)

## See Also
`.github/instructions/css-utilities.instructions.md` · `.github/instructions/frontend-design.instructions.md` · `CONTRIBUTING.md`
