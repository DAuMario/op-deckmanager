from op_deckmanager.catalog import Catalog
from op_deckmanager.deck import Deck
from op_deckmanager.deck_validator import DeckValidator
import pytest


@pytest.fixture
def validator():
    return DeckValidator(Catalog())


def test_check_card_count_returns_no_error(validator):
    deck = Deck(
        name="test",
        leader_id="test_leader_id",
        cards={"test_card": 50},
    )
    result = validator._check_card_count(deck)
    assert result == []


def test_check_card_count_returns_error(validator):
    deck = Deck(
        name="test",
        leader_id="test_leader_id",
        cards={"test_card": 40},
    )
    result = validator._check_card_count(deck)
    assert len(result) == 1
