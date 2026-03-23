import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient) -> None:
        response = client.get("/")
        assert "Soc Ops" in response.text
        assert "Start Game" in response.text
        assert "Social Bingo" in response.text

    def test_home_sets_session_cookie(self, client: TestClient) -> None:
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient) -> None:
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "Back" in response.text

    def test_board_has_25_squares(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space


class TestScavengerHuntMode:
    def test_start_scavenger_returns_checklist_with_progress(
        self, client: TestClient
    ) -> None:
        client.get("/")
        response = client.post("/start", data={"mode": "scavenger"})
        assert response.status_code == 200
        assert "Scavenger Hunt" in response.text
        assert "Scavenger checklist" in response.text
        assert "1/25" in response.text
        assert "4%" in response.text

    def test_scavenger_toggle_updates_progress(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start", data={"mode": "scavenger"})
        response = client.post("/toggle/0")
        assert response.status_code == 200
        assert "2/25" in response.text
        assert "8%" in response.text


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # The response should contain the game screen with a marked square
        assert "FREE SPACE" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        assert "Social Bingo" in response.text

    def test_reset_keeps_last_selected_mode(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start", data={"mode": "scavenger"})
        response = client.post("/reset")
        assert response.status_code == 200
        assert 'id="mode-scavenger"' in response.text
        scavenger_input = response.text.split('id="mode-scavenger"', 1)[1].split(
            ">", 1
        )[0]
        assert "checked" in scavenger_input


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
