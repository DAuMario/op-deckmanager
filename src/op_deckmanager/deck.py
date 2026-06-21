from dataclasses import dataclass, field


@dataclass
class Deck:
    """A deck with a name, a leader reference, and its cards."""

    name: str
    leader_id: str
    cards: dict[str, int] = field(default_factory=dict)


if __name__ == "__main__":
    deck = Deck(
        name="test",
        leader_id="OP01-001",
        cards={"OP01-002": 4, "OP01-003": 4, "OP01-004": 2},
    )
    print(deck)
