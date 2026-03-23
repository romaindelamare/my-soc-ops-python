import uuid
from pathlib import Path
from urllib.parse import parse_qs

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from app.game_service import GameSession, get_session
from app.models import GameMode, GameState

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Soc Ops - Social Bingo")
app.add_middleware(SessionMiddleware, secret_key="soc-ops-secret-key")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")
VALID_GAME_MODE_VALUES = {member.value for member in GameMode}


def _get_game_session(request: Request) -> GameSession:
    """Get or create a game session using cookie-based sessions."""
    if "session_id" not in request.session:
        request.session["session_id"] = uuid.uuid4().hex
    return get_session(request.session["session_id"])


def _get_requested_mode(
    request: Request, body_params: dict[str, list[str]]
) -> GameMode:
    mode_raw = request.query_params.get("mode")
    if mode_raw is None:
        mode_raw = body_params.get("mode", [GameMode.BINGO.value])[0]
    if mode_raw in VALID_GAME_MODE_VALUES:
        return GameMode(mode_raw)
    return GameMode.BINGO


def _render_game_screen(request: Request, session: GameSession) -> Response:
    return templates.TemplateResponse(
        request,
        "components/game_screen.html",
        {"session": session, "GameMode": GameMode},
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Response:
    session = _get_game_session(request)
    return templates.TemplateResponse(
        request,
        "home.html",
        {"session": session, "GameState": GameState, "GameMode": GameMode},
    )


@app.post("/start", response_class=HTMLResponse)
async def start_game(request: Request) -> Response:
    session = _get_game_session(request)
    body_params = parse_qs((await request.body()).decode("utf-8"))
    mode = _get_requested_mode(request, body_params)
    session.start_game(mode)
    return _render_game_screen(request, session)


@app.post("/toggle/{square_id}", response_class=HTMLResponse)
async def toggle_square(request: Request, square_id: int) -> Response:
    session = _get_game_session(request)
    session.handle_square_click(square_id)
    return _render_game_screen(request, session)


@app.post("/reset", response_class=HTMLResponse)
async def reset_game(request: Request) -> Response:
    session = _get_game_session(request)
    session.reset_game()
    return templates.TemplateResponse(
        request,
        "components/start_screen.html",
        {"session": session, "GameState": GameState, "GameMode": GameMode},
    )


@app.post("/dismiss-modal", response_class=HTMLResponse)
async def dismiss_modal(request: Request) -> Response:
    session = _get_game_session(request)
    session.dismiss_modal()
    return _render_game_screen(request, session)


def run() -> None:
    """Entry point for the application."""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
