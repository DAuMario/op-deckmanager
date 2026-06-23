from dataclasses import dataclass, field


@dataclass
class Deck:
    """A deck with a name, a leader reference, and its cards."""

    name: str
    leader_id: str
    cards: dict[str, int] = field(default_factory=dict)

    def add_card(self, card_id: str, count: int = 1) -> None:
        if count <= 0:
            raise ValueError(f"count must be positive, got {count}")
        self.cards[card_id] = self.cards.get(card_id, 0) + count

    def remove_card(self, card_id: str, count: int = 1) -> None:
        if count <= 0:
            raise ValueError(f"count must be positive, got {count}")
        if card_id not in self.cards:
            raise ValueError(f"card {card_id} not found in deck {self.name}")
        current_count = self.cards[card_id]
        new_count = current_count - count
        if new_count < 0:
            raise ValueError(
                f"can't remove {count} cards, only {current_count} cards found in deck {self.name}"
            )
        if new_count == 0:
            del self.cards[card_id]
        else:
            self.cards[card_id] = new_count

    def clear_deck(self) -> None:
        self.cards.clear()
