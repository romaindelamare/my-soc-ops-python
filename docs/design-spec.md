# Design Spec — Card Deck Shuffle Mode

## Overview
New game mode where each player taps to draw random question cards, one at a time, during a social gathering. Designed for quick, interactive ice-breaker moments.

## UX Flow
1. **Mode Selection** — Player selects "Card Deck Shuffle" from start screen
2. **Card Display** — A large, tappable card appears with centered question text
3. **Draw Action** — Player taps the card to draw next random question
4. **State** — Questions are drawn without repetition until deck exhausts (23 unique + free space filtered)

## Layout & Visual Design
- **Card Component** — Large square card 1:1 aspect ratio, centered on screen with question text
- **Theme** — Dark ops aesthetic matching existing design system
  - Background: `--surface` (#161616)
  - Border: `--border` (#2a2a28)
  - Text: `--fg` (#F0EDE6)
  - Accent: `--accent` (#FF4926)
- **Question Text** — Center-aligned, 1.125rem, font weight 600, word breaks enabled
- **Hint Text** — "tap for next" in muted color, tiny uppercase label
- **Empty State** — Dashed border when no card drawn yet
- **Status Bar** — Shows current count (N / Total) and remaining cards
- **Interaction** — Hover highlights border in accent color, raises elevation (surface-up bg)
- **Responsive** — Stacks properly on mobile, card resizes to maintain visibility

## Architecture

### Data Model
- `GameSession.card_deck_questions` — List of shuffled questions (23 unique)
- `GameSession.current_card_index` — Current card pointer (-1 = no card drawn)
- Properties: `card_deck_current_card`, `card_deck_has_more_cards`

### Game Logic
- `start_game(CARD_DECK)` —shuffles questions and resets index to -1
- `draw_card()` — increments index if cards remain
- State resets when returning to start screen

### API Routes
- `POST /draw-card` — Draws next card, returns full game screen

### Components
- `card_deck.html` — Main card UI with status bar
- Button-based card for HTMX interaction
- CSS classes: `card-deck-container`, `card-deck-card`, `card-deck-status-bar`

## Visual Specifications

| Element | Font | Size | Color | Weight |
|---------|------|------|-------|--------|
| Question | Instrument Sans | 1.125rem | --fg | 600 |
| Hint | Instrument Sans | 0.625rem | --muted | normal |
| Count | Instrument Sans | 0.875rem | --accent | 700 |
| Label | Instrument Sans | 0.75rem | --muted | normal |
| Remaining | Instrument Sans | 0.875rem | --fg | 700 |

## Implementation Status
- ✅ Phase 1: GameMode enum + GameSession properties
- ✅ Phase 2: Start screen mode selector
- ✅ Phase 3: Card component template
- ✅ Phase 4: Game screen routing + draw endpoint
- ✅ Phase 5: CSS styling + responsive design
- ✅ All tests passing (37/37)
- ✅ Linting passed

## Design Decisions
1. **No Free Space in Deck** — Filtered from questions; deck draws 23 unique items
2. **Square Card (1:1 aspect)** — Tappable area is generous and matches app's grid-based aesthetic
3. **Session-based State** — No persistence; resets on page reload
4. **Sharp Corners** — Matches design system (border-radius: 0)
5. **Hover State** — Minimal effect (border accent + surface-up); no shadows
6. **Empty Dashed Border** — Visual cue that card is waiting for first tap

