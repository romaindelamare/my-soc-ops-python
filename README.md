# 🎲 Soc Ops — VS Code GitHub Copilot Agent Lab

> **A hands-on workshop** where you'll level up a Social Bingo app using VS Code Agent Mode and GitHub Copilot. Ship real features. Learn real skills.

<p align="center">
  <a href="https://madebygps.github.io/vscode-github-copilot-agent-lab/"><strong>🎮 Play the Game</strong></a> &nbsp;•&nbsp;
  <a href="https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/"><strong>📚 Lab Guide</strong></a> &nbsp;•&nbsp;
  <a href="workshop/"><strong>📂 Offline Docs</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13%2B-3776AB?logo=python&logoColor=white" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/HTMX-blue?logo=htmx&logoColor=white" alt="HTMX">
  <img src="https://img.shields.io/badge/GitHub%20Copilot-required-8957E5?logo=githubcopilot&logoColor=white" alt="GitHub Copilot">
  <img src="https://img.shields.io/badge/duration-~1%20hour-brightgreen" alt="Duration ~1 hour">
</p>

---

## 🤔 What is Soc Ops?

**Soc Ops** is a Social Bingo game designed for in-person mixers. Players search the room for people who match the prompts on their card and try to get five in a row.

But the real star is **what you do with it**: this repo is a fully functioning Python/FastAPI app that serves as the playground for a ~1 hour GitHub Copilot workshop. You'll use VS Code Agent Mode to redesign the UI, add new game modes, build custom agents, and practice real-world AI-assisted development patterns — all in a codebase just complex enough to be interesting.

---

## 🎯 What You'll Learn

| # | Skill | Description |
|---|-------|-------------|
| 1 | **Context Engineering** | Teach Copilot about your project with custom instructions |
| 2 | **Agentic Primitives** | Background agents, cloud agents, and custom workflows |
| 3 | **Design-First Development** | Iterate on UI themes while you guide the creative vision |
| 4 | **Test-Driven Development** | Ship reliable features with TDD agents (Red → Green → Refactor) |

---

## 🗺️ Lab Guide

| Part | Title | Time | Description |
|------|-------|------|-------------|
| [**00**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=00-overview) | Overview & Checklist | — | Prerequisites, quick checklist, and what to expect |
| [**01**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=01-setup) | Setup & Context Engineering | 15 min | Clone, configure, and teach the AI about your project |
| [**02**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=02-design) | Design-First Frontend | 15 min | Redesign the whole UI with creative themes in Agent Mode |
| [**03**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=03-quiz-master) | Custom Quiz Master | 10 min | Create your own quiz themes with a custom Copilot agent |
| [**04**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=04-multi-agent) | Multi-Agent Development | 20 min | Build new game modes with TDD agents working in concert |

> 📝 All lab guides are available offline in the [`workshop/`](workshop/) folder.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | [Python 3.13](https://www.python.org/) + [FastAPI](https://fastapi.tiangolo.com/) |
| Templating | [Jinja2](https://jinja.palletsprojects.com/) |
| Interactivity | [HTMX](https://htmx.org/) |
| Package Manager | [uv](https://docs.astral.sh/uv/) |
| Deploy | GitHub Pages (auto on push to `main`) |

---

## ⚡ Quick Start

### Prerequisites

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) package manager
- VS Code v1.107+ with GitHub Copilot (Pro, Business, or Enterprise)

### Option A — Local Dev

```bash
# 1. Use this template to create your own repo, then clone it
git clone https://github.com/<your-username>/my-soc-ops-python
cd my-soc-ops-python

# 2. Install dependencies
uv sync

# 3. Start the app
uv run uvicorn app.main:app --reload
```

Then open **http://localhost:8000** in your browser.

### Option B — DevContainer / Codespaces

This repo ships with a preconfigured devcontainer at `.devcontainer/devcontainer.json` — zero local setup required.

- **Local VS Code**: Reopen the repo in container when prompted
- **GitHub Codespaces**: Click **Code → Codespaces → Create codespace on main**

---

## 🧪 Test & Lint

```bash
# Run tests
uv run pytest

# Lint & format
uv run ruff check .
uv run ruff format .
```

---

## 💡 Workshop Tips

1. **Keep the browser open** — watch the app update live as agents make changes
2. **Commit early and often** — save working states so you can always roll back
3. **Use Checkpoints** — VS Code chat Checkpoints let you undo unexpected agent changes
4. **Iterate on plans** — ask Copilot to revise its plan 2–3 times before it starts coding

---

## 🔗 Resources

- [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot](https://github.com/features/copilot)
- [Awesome Copilot](https://github.com/github/awesome-copilot)
- [VS Code on YouTube](https://www.youtube.com/code)
