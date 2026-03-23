import random
from dataclasses import dataclass, field

from app.data import QUESTIONS
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
    card_deck_questions: list[str] = field(default_factory=list)
    current_card_index: int = -1

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

    @property
    def card_deck_current_card(self) -> str | None:
        """Get the current card text, or None if no card has been drawn."""
        if 0 <= self.current_card_index < len(self.card_deck_questions):
            return self.card_deck_questions[self.current_card_index]
        return None

    @property
    def card_deck_has_more_cards(self) -> bool:
        """Check if there are more cards to draw."""
        return (self.current_card_index + 1) < len(self.card_deck_questions)

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.mode = mode
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False

        if mode == GameMode.CARD_DECK:
            self.card_deck_questions = random.sample(QUESTIONS, len(QUESTIONS))
            self.current_card_index = -1
            self.board = []
        else:
            self.board = generate_board()
            self.card_deck_questions = []
            self.current_card_index = -1

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

    def draw_card(self) -> None:
        """Draw the next card from the deck."""
        if self.mode == GameMode.CARD_DECK and self.card_deck_has_more_cards:
            self.current_card_index += 1

    def reshuffle_deck(self) -> None:
        """Reshuffle the deck and reset to the beginning."""
        if self.mode == GameMode.CARD_DECK:
            self.card_deck_questions = random.sample(QUESTIONS, len(QUESTIONS))
            self.current_card_index = -1

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.card_deck_questions = []
        self.current_card_index = -1

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
