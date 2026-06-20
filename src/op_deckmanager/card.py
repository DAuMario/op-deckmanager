from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Card:
    """Base Class for all Cards in the One Piece TCG"""

    card_id: str
    name: str
    card_type: str
    color: list[str]
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


@dataclass
class Leader(Card):
    """Leader Type Class with Life, Power, Effects etc."""

    life: int = 0
    power: int = 0
    attributes: list[str] = field(default_factory=list)
    effects: list[str] = field(default_factory=list)


@dataclass
class Event(Card):
    """Event Type Card"""

    cost: int = 0
    main_effect: Optional[str] = None
    counter_effect: Optional[str] = None
    trigger: Optional[str] = None
    counter: int = 0  # 0 = event has no counter effect


if __name__ == "__main__":
    buggy_event = Event(
        card_id="OP16-057",
        name="Captain Buggy's Our Savior!!",
        card_type="Event",
        color=["Blue"],
        card_block=5,
        rarity="C",
        affiliations=["Impel Down"],
        cost=1,
        counter_effect="If you have 2 or more [Prisoner of Impel Down] cards, up to 1 of your Leader or Character cards gains +4000 Power during this Battle",
        trigger="Draw 2 Cards and trash 1 card from your Hand",
        counter=4000,
    )
    print(buggy_event)
