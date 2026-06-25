from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck
from op_deckmanager.deck_validator import DeckValidator
from op_deckmanager.card import Leader, Character
from op_deckmanager.ban_list import BanList
import pytest


@pytest.fixture
def validator():
    return DeckValidator(Catalog(), BanList())


def build_valid_deck() -> tuple[Catalog, Deck]:
    catalog = Catalog()
    leader = Leader(
        card_id="leader-01", name="test_name", card_type="Leader", color=["Red"]
    )
    catalog.add_card(leader)
    cards: dict[str, int] = {}
    for i in range(13):
        card_id = f"character-{i}"
        character = Character(
            card_id=card_id, name="test_name", card_type="Character", color=["Red"]
        )
        catalog.add_card(character)
        cards[card_id] = 2 if i == 12 else 4
    deck = Deck(name="test", leader_id=leader.card_id, cards=cards)
    return catalog, deck


def test_check_card_count_returns_no_error(validator):
    deck = Deck(name="test", leader_id="test_leader_id", cards={"test_card": 50})
    result = validator._check_card_count(deck)
    assert result == []


def test_check_card_count_returns_error(validator):
    deck = Deck(name="test", leader_id="test_leader_id", cards={"test_card": 40})
    result = validator._check_card_count(deck)
    assert len(result) == 1


def test_check_max_copies_returns_no_error(validator):
    deck = Deck(name="test", leader_id="test_leader_id", cards={"test_card": 4})
    result = validator._check_max_copies(deck)
    assert result == []


def test_check_max_copies_returns_error(validator):
    deck = Deck(name="test", leader_id="test_leader_id", cards={"test_card": 5})
    result = validator._check_max_copies(deck)
    assert len(result) == 1


def test_check_leader_returns_no_error():
    catalog = Catalog()
    test_leader = Leader(
        card_id="test_card_id", name="test_name", card_type="test", color=["test_color"]
    )
    catalog.add_card(test_leader)
    deck = Deck(name="test", leader_id=test_leader.card_id, cards={})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_leader(deck)
    assert result == []


def test_check_leader_returns_error_for_nonexistent_id(validator):
    deck = Deck(name="test", leader_id="does_not_exist", cards={})
    result = validator._check_leader(deck)
    assert len(result) == 1


def test_check_leader_returns_card_is_not_leader_type():
    catalog = Catalog()
    test_card = Character(
        card_id="test_card_id", name="test_name", card_type="test", color=["test_color"]
    )
    catalog.add_card(test_card)
    deck = Deck(name="test", leader_id=test_card.card_id, cards={})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_leader(deck)
    assert len(result) == 1


def test_check_color_identity_returns_no_error():
    catalog = Catalog()
    leader = Leader(
        card_id="leader-01", name="test_name", card_type="Leader", color=["Red"]
    )
    character = Character(
        card_id="character-01", name="test_name", card_type="Character", color=["Red"]
    )
    catalog.add_card(leader)
    catalog.add_card(character)
    deck = Deck(name="test", leader_id=leader.card_id, cards={character.card_id: 1})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_color_identity(deck)
    assert result == []


def test_check_color_identity_returns_error():
    catalog = Catalog()
    leader = Leader(
        card_id="leader-01", name="test_name", card_type="Leader", color=["Red"]
    )
    character = Character(
        card_id="character-01", name="test_name", card_type="Character", color=["Blue"]
    )
    catalog.add_card(leader)
    catalog.add_card(character)
    deck = Deck(name="test", leader_id=leader.card_id, cards={character.card_id: 1})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_color_identity(deck)
    assert len(result) == 1


def test_check_color_identity_returns_no_error_with_multiple_colored_leader():
    catalog = Catalog()
    leader = Leader(
        card_id="leader-01",
        name="test_name",
        card_type="Leader",
        color=["Red", "Green"],
    )
    character = Character(
        card_id="character-01", name="test_name", card_type="Character", color=["Green"]
    )
    catalog.add_card(leader)
    catalog.add_card(character)
    deck = Deck(name="test", leader_id=leader.card_id, cards={character.card_id: 1})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_color_identity(deck)
    assert result == []


def test_check_color_identity_skips_when_leader_invalid():
    catalog = Catalog()
    leader = Character(
        card_id="leader-01", name="test_name", card_type="Leader", color=["Red"]
    )
    character = Character(
        card_id="character-01", name="test_name", card_type="Character", color=["Blue"]
    )
    catalog.add_card(leader)
    catalog.add_card(character)
    deck = Deck(name="test", leader_id=leader.card_id, cards={character.card_id: 1})
    validator = DeckValidator(catalog, BanList())
    result = validator._check_color_identity(deck)
    assert result == []


def test_validate_returns_no_error():
    catalog, deck = build_valid_deck()
    validator = DeckValidator(catalog, BanList())
    result = validator.validate(deck)
    assert result == []


def test_validate_returns_multiple_errors():
    catalog, deck = build_valid_deck()
    card = Character(
        card_id="character-000", name="test_name", card_type="Character", color=["Blue"]
    )
    catalog.add_card(card)
    deck.cards[card.card_id] = 1
    validator = DeckValidator(catalog, BanList())
    result = validator.validate(deck)
    assert len(result) == 2


def test_check_banned_card_is_not_banned():
    catalog = Catalog()
    deck = Deck(name="test", leader_id="test_leader_id", cards={"safe_id": 1})
    ban_list = BanList(banned={"banned_id"})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_banned(deck)
    assert result == []


def test_check_banned_card_is_banned():
    catalog = Catalog()
    deck = Deck(name="test", leader_id="test_leader_id", cards={"banned_id": 1})
    ban_list = BanList(banned={"banned_id"})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_banned(deck)
    assert len(result) == 1


def test_check_restricted_unlisted_card_is_allowed():
    catalog = Catalog()
    deck = Deck(name="test", leader_id="test_leader_id", cards={"safe_id": 2})
    ban_list = BanList(restricted={"restricted_id"})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_restricted(deck)
    assert result == []


def test_check_restricted_multiple_copies_returns_error():
    catalog = Catalog()
    deck = Deck(name="test", leader_id="test_leader_id", cards={"restricted_id": 2})
    ban_list = BanList(restricted={"restricted_id"})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_restricted(deck)
    assert len(result) == 1


def test_check_restricted_allows_single_copy():
    catalog = Catalog()
    deck = Deck(name="test", leader_id="test_leader_id", cards={"restricted_id": 1})
    ban_list = BanList(restricted={"restricted_id"})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_restricted(deck)
    assert result == []


def test_check_banned_pairs_both_cards_in_deck():
    catalog = Catalog()
    deck = Deck(
        name="test",
        leader_id="test_leader_id",
        cards={"banned_pair_1": 1, "banned_pair_2": 1},
    )
    ban_list = BanList(banned_pairs={frozenset({"banned_pair_1", "banned_pair_2"})})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_banned_pairs(deck)
    assert len(result) == 1


def test_check_banned_pairs_only_one_in_deck():
    catalog = Catalog()
    deck = Deck(
        name="test",
        leader_id="test_leader_id",
        cards={"banned_pair_1": 1, "safe_id": 1},
    )
    ban_list = BanList(banned_pairs={frozenset({"banned_pair_1", "banned_pair_2"})})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_banned_pairs(deck)
    assert result == []


def test_check_banned_pairs_no_copy_in_deck():
    catalog = Catalog()
    deck = Deck(
        name="test",
        leader_id="test_leader_id",
        cards={"safe_id_1": 1, "safe_id_2": 1},
    )
    ban_list = BanList(banned_pairs={frozenset({"banned_pair_1", "banned_pair_2"})})
    validator = DeckValidator(catalog, ban_list)
    result = validator._check_banned_pairs(deck)
    assert result == []
