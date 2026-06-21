from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck


class DeckValidator:
    """Validates a deck against the One Piece TCG rules."""

    def __init__(self, catalog: Catalog) -> None:
        self.catalog = catalog

    def _check_card_count(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        total = sum(deck.cards.values())
        if total != 50:
            errors.append(f"Deck must contain exactly 50 Cards, but has {total}")
        return errors
