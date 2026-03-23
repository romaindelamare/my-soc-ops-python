from app.questions import TECH_LIFE_QUESTIONS


def test_tech_life_questions_count() -> None:
    assert len(TECH_LIFE_QUESTIONS) == 24


def test_tech_life_questions_are_strings() -> None:
    assert all(isinstance(q, str) and q for q in TECH_LIFE_QUESTIONS)


def test_tech_life_questions_unique() -> None:
    assert len(set(TECH_LIFE_QUESTIONS)) == len(TECH_LIFE_QUESTIONS)
