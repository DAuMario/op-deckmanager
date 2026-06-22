from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck
from op_deckmanager.card import Leader


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

    def _check_leader(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        card = self.catalog.get_card(deck.leader_id)
        if card is None:
            errors.append(f"{deck.leader_id} does not exist.")
        elif not isinstance(card, Leader):
            errors.append(f"{card.card_id} ({card.name}) is not a Leader.")
        return errors

    def _check_color_identity(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        leader = self.catalog.get_card(deck.leader_id)
        if not isinstance(leader, Leader):
            return errors
        for card_id in deck.cards:
            card = self.catalog.get_card(card_id)
            if card is None:
                continue
            if not card.color:
                continue
            if card.color[0] not in leader.color:
                errors.append(
                    f"{card.card_id} ({card.name}) has color {card.color[0]}, which is not in the leader's colors {leader.color}."
                )
        return errors
