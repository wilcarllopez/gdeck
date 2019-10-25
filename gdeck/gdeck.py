class Card:
    """Standard playing card.
    Attributes:
        suit: string spades,hearts,diamonds,clubs
        rank: string 1-10,jack,queen,king
    """
    def __init__(self, rank, suit):
        """Initializes the object Card"""
        self.rank = rank
        self.suit = suit


    def __repr__(self):
        """Returns a string of Card with rank and suit"""
        return str(f'{self.rank} of {self.suit}')

class Deck:
    """Class for a regular decks"""
    suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
    rank = ["Ace", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)",
            "Ten(10)", "Jack", "Queen", "King"]

    def __init__(self):
        """Initializes the object Deck"""
        self.cards = [Card(r, s) for r in Deck.rank for s in Deck.suit]
        self.counter = 0

    def __getitem__(self, position):
        """Returns sliced object"""
        return self.cards[position]

    def __len__(self):
        """Counts the element inside the object"""
        return len(self.cards)

    def __iter__(self):
        """Returns an iterator object"""
        return self

    def __next__(self):
        """Returns the next element"""
        if self.counter >= len(self.cards):
            raise StopIteration
        current = self.cards[self.counter]
        self.counter += 1
        return current

    def __repr__(self):
        """Returns a string of cards in a string list"""
        return str(self.cards)