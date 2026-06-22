# One Piece TCG Deck Manager

Tool to manage and analyse One Piece TCG Decks with AI-supported tips for deckbuilding. 

## Status

In development

## Features

- Central card catalog for looking up cards by ID
- Deck validation against the core deckbuilding rules

## Features (planned)

- Deck management methods (Add and remove Cards)
- Block rotation rules and banlists implementation
- Statistical analysis of Decks (Cost curve, Counter overview, etc)
- API connection for building card catalog
- Frontend for ease of use
- AI-supported tips for deckbuilding via LLM-API

## Setup

Requires Python 3.13 or newer.

```bash
# Clone the repository
git clone https://github.com/DAuMario/op-deckmanager.git
cd op-deckmanager

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# Install the project (editable) and dev dependencies
pip install -e .
pip install -r requirements-dev.txt

# Run the tests
pytest
```