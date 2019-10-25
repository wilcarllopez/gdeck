import pytest
from random import choice
from gdeck.gdeck import *

suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
rank = ["Ace", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)","Ten(10)", "Jack", "Queen", "King"]

def test_card():
    assert (Card(s,r) for s in suit for r in rank)

def test_deck_size():
    #assert len(Deck()) == 52
    pass

def test_choice():
    deck = Deck()
    assert choice(deck)

def test_deck():
    cards = []
    for s in suit:
        for r in rank:
            cards.append("{} of {}".format(r,s))
    assert ((Deck()) == cards)
if __name__ == '__main__':
    pytest.main()
