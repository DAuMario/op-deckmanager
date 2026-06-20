from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Card:
    """Base Class for all Cards in the One Piece TCG"""

    card_id: str
    name: str
    card_type: str
    color: str
    card_block: Optional[int] = None
    rarity: Optional[str] = None
    affiliations: list[str] = field(default_factory=list)


@dataclass
class Character(Card):
    """Character Type Class, with Power, Counter, Effects etc."""

    cost: int = 0
    power: int = 0
    counter: int = 0  # 0 = no counter printed on card
    attributes: list[str] = field(
        default_factory=list
    )  # usually characters only have 1 attribute, but edge cases exist
    effects: list[str] = field(
        default_factory=list
    )  # for now effects as str; gonna update later if needed
    trigger: Optional[str] = None
    has_blocker: bool = False


if __name__ == "__main__":
    luffy = Character(
        card_id="OP16-012",
        name="Monkey D. Luffy",
        card_type="Character",
        color="Red",
        card_block=4,
        rarity="SR",
        affiliations=["Straw Hat Crew"],
        cost=5,
        power=6000,
        counter=1000,
        attributes=["Strike"],
    )
    print(luffy)
