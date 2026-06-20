from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Card:
    card_id: str
    name: str
    card_type: str
    color: str
    card_block: Optional[int] = None
    rarity: Optional[str] = None
    affiliations: list[str] = field(default_factory=list)





if __name__ == "__main__":
    luffy = Card(
        card_id="OP16-012",
        name="Monkey D. Luffy",
        card_type="Character",
        color="Red",
        card_block=4,
        rarity="SR",
        affiliations=["Straw Hat Crew"],
    )
    print(luffy)