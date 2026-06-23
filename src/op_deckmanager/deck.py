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
