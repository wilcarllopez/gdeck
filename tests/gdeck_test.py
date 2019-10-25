import pytest
from gdeck import Card
from gdeck import Deck


deck = Deck()

def test_card:
    card = Card("Hearts","Ace")
    assert print(card) == "Ace of Hearts"

if __name__ == '__main__':
    pytest.main()
