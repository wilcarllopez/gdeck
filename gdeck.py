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
    rank = ["Ace", "One", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Eight(8)", "Nine(9)",
            "Ten(10)", "Jack", "Queen", "King"]
    def __init__(self, suit, rank):
        self.cards=[]
        self.build(suit,rank)

    def build(self, suit, rank):
        self.count = 0
        return [self.cards.append(Card(s, r)) for s in suit for r in rank]

    def __getitem__(self, position):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)

    def __next__(self):
        if self.count >= len(self.cards):
            raise StopIteration
        current = self.cards[self.count]
        self.count += 1
        return current

    def __repr__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"
            return (s)
