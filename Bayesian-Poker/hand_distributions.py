import itertools
import random

class Card():
    suits = { 'Hearts': '♥', 'Spades': '♣', 'Clubs': '♠', 'Diamonds': '♦'}
    ranks = dict(zip(range(1, 14), '123456789JQKA'))
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return Card.ranks[self.rank] + Card.suits[self.suit]

    def __lt__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank

class Hand():
    size = 5
    def __init__(self, cards):
        if len(cards) != Hand.size:
            raise IndexError(f'Hands must be composed of {Hand.size} Cards')
        
        self.cards = sorted(cards)
        self.ranks = {card.rank for card in cards}
        self.suits = {card.suit for card in cards}

    def __str__(self):
        return str(list(map(str, self.cards)))

    @property
    def pairs(self):
        if len(self.ranks) == (Card.size - 1):
            pass
        else:
            pass
    
    @property
    def double_pair(self):
        return len(self.ranks) == (Card.size - 2)

deck = [Card(rank, suit) for rank, suit in itertools.product(Card.ranks, Card.suits)]



def main():
    hand = Hand(random.sample(deck, 5))
    print(hand)
    print(hand.suits)
    print(hand.ranks)

if __name__ == '__main__':
    main()