from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    mode: GameMode = GameMode.BINGO
    game_state: GameState = GameState.START
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.mode == GameMode.BINGO and self.game_state == GameState.BINGO

    @property
    def has_scavenger_complete(self) -> bool:
        return self.mode == GameMode.SCAVENGER and self.game_state == GameState.BINGO

    @property
    def scavenger_marked_count(self) -> int:
        return sum(1 for square in self.board if square.is_marked)

    @property
    def scavenger_total_count(self) -> int:
        return len(self.board)

    @property
    def scavenger_progress_percent(self) -> int:
        if self.scavenger_total_count == 0:
            return 0
        return int((self.scavenger_marked_count * 100) / self.scavenger_total_count)

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.mode = mode
        self.board = generate_board()
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.mode == GameMode.BINGO and self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

        if self.mode == GameMode.SCAVENGER and all(
            square.is_marked for square in self.board
        ):
            self.winning_line = None
            self.game_state = GameState.BINGO
            self.show_bingo_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
