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

## See Also
`.github/instructions/css-utilities.instructions.md` · `.github/instructions/frontend-design.instructions.md` · `CONTRIBUTING.md`
