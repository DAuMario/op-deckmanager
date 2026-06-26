from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck
from op_deckmanager.card import Leader
from op_deckmanager.ban_list import BanList
from op_deckmanager.block_rotation import BlockRotation


class DeckValidator:
    """Validates a deck against the One Piece TCG rules."""

    def __init__(
        self, catalog: Catalog, ban_list: BanList, block_rotation: BlockRotation
    ) -> None:
        self.catalog = catalog
        self.ban_list = ban_list
        self.block_rotation = block_rotation

    def validate(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        errors.extend(self._check_card_count(deck))
        errors.extend(self._check_max_copies(deck))
        errors.extend(self._check_leader(deck))
        errors.extend(self._check_color_identity(deck))
        errors.extend(self._check_banned(deck))
        errors.extend(self._check_restricted(deck))
        errors.extend(self._check_banned_pairs(deck))
        return errors

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

    def _check_banned(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        for card_id in deck.cards:
            if card_id in self.ban_list.banned:
                card = self.catalog.get_card(card_id)
                name = card.name if card else card_id
                errors.append(f"{card_id} ({name}) is currently banned.")
        return errors

    def _check_restricted(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        for card_id, count in deck.cards.items():
            if card_id in self.ban_list.restricted and count > 1:
                card = self.catalog.get_card(card_id)
                name = card.name if card else card_id
                errors.append(f"{card_id} ({name}) is currently restricted to 1 copy.")
        return errors

    def _check_banned_pairs(self, deck: Deck) -> list[str]:
        errors: list[str] = []
        for pair in self.ban_list.banned_pairs:
            if all(card_id in deck.cards for card_id in pair):
                pair_list = list(pair)
                card1 = self.catalog.get_card(pair_list[0])
                name1 = card1.name if card1 else pair_list[0]
                card2 = self.catalog.get_card(pair_list[1])
                name2 = card2.name if card2 else pair_list[1]
                errors.append(
                    f"{pair_list[0]} ({name1}) and {pair_list[1]} ({name2}) can't be in the same deck together."
                )
        return errors
