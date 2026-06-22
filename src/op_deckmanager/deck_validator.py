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
            errors.append(f"Deck must contain exactly 50 Cards, but has {total}.")
        return errors

    def _check_max_copies(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        for card_id, count in deck.cards.items():
            if count > 4:
                errors.append(
                    f"Only 4 Copies per Card allowed, Card {card_id} is {count} times in the Deck."
                )
        return errors
