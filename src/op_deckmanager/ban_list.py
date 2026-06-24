from dataclasses import dataclass, field


@dataclass
class BanList:
    banned: set[str] = field(default_factory=set)
    restricted: set[str] = field(default_factory=set)
    banned_pairs: set[frozenset[str]] = field(default_factory=set)
