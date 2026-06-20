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
    # usually characters only have 1 attribute, but edge cases exist
    attributes: list[str] = field(default_factory=list)
    # for now effects as str; gonna update later if needed
    effects: list[str] = field(default_factory=list)
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
    """Event Type Card with Cost, Main and/or Counter Effects"""

    cost: int = 0
    main_effect: Optional[str] = None
    counter_effect: Optional[str] = None
    trigger: Optional[str] = None
    counter: int = 0  # 0 = event has no counter effect


@dataclass
class Stage(Card):
    """Stage Type Card with Cost, Effects and Trigger"""

    cost: int = 0
    effects: list[str] = field(default_factory=list)
    trigger: Optional[str] = None


if __name__ == "__main__":
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
    print(sunny)
