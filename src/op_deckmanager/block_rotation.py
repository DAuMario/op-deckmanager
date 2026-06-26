from dataclasses import dataclass, field


@dataclass
class BlockRotation:
    legal_blocks: set[str] = field(default_factory=set)
    # "Manga-rares" and "Superparallel" cards are exempt from the block rotation
    block_exemption: set[str] = field(default_factory=set)
    # Some cards get treated as another block, specified by Bandai
    block_overrides: dict[str, str] = field(default_factory=dict)
