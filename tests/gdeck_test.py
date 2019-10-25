import pytest
from gdeck import *

suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
rank = ["Ace", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)","Ten(10)", "Jack", "Queen", "King"]

def test_card():
    for s in suit:
        for r in rank:
            assert Card(s,r)

def test_deck_size():
    #assert len(Deck())
    pass

if __name__ == '__main__':
    pytest.main()
