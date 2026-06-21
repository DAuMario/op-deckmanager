from dataclasses import dataclass, field
from op_deckmanager.card import Leader


@dataclass
class Deck:
    """A deck with a name, a leader reference, and its cards."""

    name: str
    leader_id: str
    cards: dict[str, int] = field(default_factory=dict)


if __name__ == "__main__":
    leader = Leader(
        card_id="OP01-001",
        name="Monkey D. Luffy",
        card_type="Leader",
        color=["Red"],
        life=5,
        power=5000,
    )
    print(leader)

    deck = Deck(
        name="test",
        leader_id=leader.card_id,
        cards={"OP01-002": 4, "OP01-003": 4, "OP01-004": 2},
    )
    print(deck)
