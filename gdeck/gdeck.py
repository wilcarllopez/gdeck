class Card:
    """Standard playing card.
    Attributes:
        suit: string spades,hearts,diamonds,clubs
        rank: string 1-10,jack,queen,king
    """
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)

class Deck:
    """Class for a regular decks"""
    suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
    rank = ["Ace", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)",
            "Ten(10)", "Jack", "Queen", "King"]

    def __init__(self):
        self.cards = []
        self.cards.append(Card(s, r) for s in Deck.suit for r in Deck.rank)
        self.counter = 0

    def __getitem__(self, position):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)

    def __next__(self):
        if self.counter >= len(self.cards):
            raise StopIteration
        current = self.cards[self.counter]
        self.counter += 1
        return current

    def __repr__(self):
        s = ""
        for i in self.cards:
            s += str(i) + "\n"
        return s