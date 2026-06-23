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


def test_remove_card_partial():
    deck = Deck(name="testdeck", leader_id="test_leader", cards={"test_card": 3})
    deck.remove_card("test_card", 1)
    assert deck.cards["test_card"] == 2


def test_remove_card_to_zero():
    deck = Deck(name="testdeck", leader_id="test_leader", cards={"test_card": 3})
    deck.remove_card("test_card", 3)
    assert "test_card" not in deck.cards


def test_remove_card_not_in_deck():
    deck = Deck(name="testdeck", leader_id="test_leader")
    with pytest.raises(ValueError):
        deck.remove_card("test_card")


def test_remove_card_too_many():
    deck = Deck(name="testdeck", leader_id="test_leader", cards={"test_card": 3})
    with pytest.raises(ValueError):
        deck.remove_card("test_card", 5)


def test_remove_card_invalid_count():
    deck = Deck(name="testdeck", leader_id="test_leader", cards={"test_card": 3})
    with pytest.raises(ValueError):
        deck.remove_card("test_card", -3)
