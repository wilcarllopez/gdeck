import pytest
import random
from gdeck.gdeck import *

suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
rank = ["Ace", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)","Ten(10)", "Jack", "Queen", "King"]
cards = [Card(r,s) for r in rank for s in suit]

def test_card():
    """Tests the class Card()"""
    assert (Card(s,r) for s in suit for r in rank)

def test_deck_size():
    """Tests the len of the deck"""
    assert len(Deck()) == len(cards)

def test_deck_iter():
    """Tests the dunder iter method"""
    with pytest.raises(StopIteration):
        deck = Deck()
        for i in iter(deck):
            next(deck)
        next(deck)

def test_deck_slice():
    """Tests the object Deck() slicing"""
    assert f"{Deck()[:5:]}" == str(cards[:5:])

def test_deck_repr():
    """Tests the dunder repr of Deck()"""
    assert str(Deck()) == str([Card(r,s) for r in rank for s in suit])

def test_def_choice():
    """Tests the random.choice if it returns a Card object"""
    assert isinstance(random.choice(Deck()),Card)

if __name__ == '__main__':
    pytest.main()