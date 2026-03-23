from typing import Final

FREE_SPACE: Final = "FREE SPACE"

QUESTIONS: Final[list[str]] = [
    "has named a device something dramatic",
    "has opened 30+ browser tabs at once",
    "has fixed something by turning it off and on",
    "uses dark mode in at least 3 apps",
    "has a charger in their bag right now",
    "has sent a message with a typo and left it",
    "can explain their job using only emoji",
    "has said it works on my machine",
    "has used ai to rewrite a text",
    "has more screenshots than photos",
    "can recommend a bizarre but useful app",
    "has a keyboard shortcut they guard like treasure",
    "has joined a call while muted and kept talking",
    "has a playlist for focus mode",
    "has rage-closed a tab and reopened it instantly",
    "has ever rebooted and prayed",
    "can mime a loading spinner for 5 seconds",
    "has accidentally replied all",
    "has a side project that is 80 percent ideas",
    "can pitch a fake startup in 10 seconds",
    "wins a round of rock-paper-scissors",
    "teaches a 5-second shortcut",
    "shares the weirdest error message they remember",
    "has solved a problem with a wildly unrelated trick",
]

# Tech Life Bingo — replaces the default question pool
from app.questions import TECH_LIFE_QUESTIONS  # noqa: E402

QUESTIONS = TECH_LIFE_QUESTIONS  # type: ignore[assignment]
