import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        """
        Code representation of one card

        :return: repr string
        """
        return f"Card('{self.rank}', '{self.suit}')"


class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    # constructor
    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    # called when property used
    @property  # decorate dealer with property
    def dealer(self): # getter property
        return self._dealer

    # called when property assigned to
    @dealer.setter
    def dealer(self, dealer): # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer}/{len(self)}"

    def __repr__(self):
        # CardDeck('dealer')
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.dealer}')"
