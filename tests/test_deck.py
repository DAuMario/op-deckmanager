from op_deckmanager.deck import Deck
import pytest


def test_add_card_new():
    deck = Deck(name="testdeck", leader_id="test_leader")
    deck.add_card("CARD-001")
    assert deck.cards["CARD-001"] == 1


def test_add_card_existing():
    deck = Deck(name="testdeck", leader_id="test_leader", cards={"CARD-001": 2})
    deck.add_card("CARD-001")
    assert deck.cards["CARD-001"] == 3


def test_add_card_invalid_count():
    deck = Deck(name="testdeck", leader_id="test_leader")
    with pytest.raises(ValueError):
        deck.add_card("CARD-001", -3)
