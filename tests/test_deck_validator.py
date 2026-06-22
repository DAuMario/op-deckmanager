from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck
from op_deckmanager.deck_validator import DeckValidator
from op_deckmanager.card import Leader, Character
import pytest


@pytest.fixture
def validator():
    return DeckValidator(Catalog())


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
    validator = DeckValidator(catalog)
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
    validator = DeckValidator(catalog)
    result = validator._check_leader(deck)
    assert len(result) == 1
