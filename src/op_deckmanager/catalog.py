from op_deckmanager.card import Card, Character, Leader, Stage
from typing import Optional


class Catalog:
    """Holds all Cards, looked up by card_id"""

    def __init__(self) -> None:
        self.cards: dict[str, Card] = {}

    def add_card(self, card: Card) -> None:
        self.cards[card.card_id] = card

    def get_card(self, card_id: str) -> Optional[Card]:
        return self.cards.get(card_id)


if __name__ == "__main__":
    catalog = Catalog()

    luffy = Leader(
        card_id="OP-001",
        name="Luffy",
        card_type="Leader",
        color=["Red"],
        rarity="L",
        affiliations=["Straw Hat Crew"],
        attributes=["Strike"],
        effects=["this is only a test", "this is another test"],
    )

    sunny = Stage(
        card_id="ST14-017",
        name="Thousand Sunny",
        card_type="Stage",
        color=["Black"],
        card_block=2,
        rarity="C",
        affiliations=["Straw Hat Crew"],
        cost=1,
        effects=[
            "All of your black {Straw Hat Crew} Type Characters gain +1 Cost",
            "On Play: If you Leader has the {Straw Hat Crew} type, draw 1 card",
        ],
    )

    nami = Character(
        card_id="OP01-004",
        name="Nami",
        card_type="Character",
        rarity="SR",
        color=["Red"],
        affiliations=["Straw Hat Crew", "East Blue"],
        cost=4,
        attributes=["Strike"],
    )

    catalog.add_card(luffy)
    catalog.add_card(nami)
    catalog.add_card(sunny)

    print(catalog.get_card("OP01-004"))
    print(catalog.get_card("OP-001"))
    print(catalog.get_card("ST14-017"))
    print(catalog.get_card("luffy"))
