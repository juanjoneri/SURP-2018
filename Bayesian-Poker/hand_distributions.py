import itertools
import random
import collections

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

    @staticmethod
    def highest(cards):
        # returns the highest card by rank in a collection
        return max(cards)

class Hand():
    size = 5
    def __init__(self, cards):
        if len(cards) != Hand.size:
            raise IndexError(f'Hands must be composed of {Hand.size} Cards')
        
        self.cards = sorted(cards)
        self.ranks = {card.rank for card in self.cards}
        self.suits = {card.suit for card in self.cards}

    def __str__(self):
        return str(list(map(str, self.cards)))

    '''
    Every Hand Type returns the highest card in the hand if the game is present and None otherwise
    '''
    @property
    def flush(self):
        if len(self.ranks) == 1:
            return Card.highest(self.cards)
        return None
    
    @property
    def straight(self):
        if list(sorted(self.ranks)) == range(min(self.ranks), max(self.ranks) + 1):
            return Card.highest(self.cards)
        return None

    @property
    def busted(self):
        if len(self.ranks) == Hand.size and not self.flush and not self.straight:
            return Card.highest(self.cards)
    
    @property
    def double_pair(self):
        return len(self.ranks) == (Card.size - 2)

deck = [Card(rank, suit) for rank, suit in itertools.product(Card.ranks, Card.suits)]

def main():
    hand = Hand(random.sample(deck, 5))
    print(hand)
    print(Card.highest(hand.cards))
    print(hand.suits)
    print(hand.ranks)
    print(hand.busted)

if __name__ == '__main__':
    main()