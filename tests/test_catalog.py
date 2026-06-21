from op_deckmanager.catalog import Catalog
from op_deckmanager.card import Character
import pytest


@pytest.fixture
def catalog():
    return Catalog()


@pytest.fixture
def test_character():
    return Character(
        card_id="Test ID",
        name="Test Name",
        card_type="Test Typ",
        color=["Testfarbe"],
    )


def test_get_card_returns_correct_card(catalog, test_character):

    catalog.add_card(test_character)
    result = catalog.get_card("Test ID")
    assert result is test_character


def test_get_card_returns_no_available_card(catalog):
    result = catalog.get_card("Test ID")
    assert result is None
