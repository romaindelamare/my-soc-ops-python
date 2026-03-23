from app.data import FREE_SPACE, QUESTIONS
from app.questions import TECH_LIFE_QUESTIONS


def test_questions_is_tech_life() -> None:
    assert QUESTIONS == TECH_LIFE_QUESTIONS


def test_questions_has_24_items() -> None:
    assert len(QUESTIONS) == 24


def test_free_space_is_string() -> None:
    assert isinstance(FREE_SPACE, str)
    assert len(FREE_SPACE) > 0
