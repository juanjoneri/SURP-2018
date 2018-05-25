import itertools
import random
import collections

class Deck():
    suits = { 'Hearts': '♥', 'Spades': '♣', 'Clubs': '♠', 'Diamonds': '♦'}
    ranks = {i: str(i) for i in range(2, 11)}
    ranks.update({11: 'J', 12: 'Q', 13: 'K', 14: 'A'})

    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in itertools.product(self.ranks, self.suits)]
    
    def random_hand(self, size):
        return Hand(random.sample(self.cards, size))

class Card():
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return Deck.ranks[self.rank] + Deck.suits[self.suit]

    def __lt__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank

    def __hash__(self):
        return hash(self.rank)

    @staticmethod
    def highest(cards):
        # returns the highest card by rank in a collection
        return max(cards)

class Hand():

    def __init__(self, cards):
        self.size = len(cards)
        
        self.cards = sorted(cards)
        self.counts = collections.Counter(self.cards).items()

        self.ranks = {card.rank for card in self.cards}
        self.suits = {card.suit for card in self.cards}
        
    @property
    def groups(self):
        self._groups = collections.defaultdict(list)
        for card, count in self.counts:
            self._groups[count].append(tuple(filter(lambda x: x == card, self.cards)))
        return self._groups

    def __str__(self):
        return str(list(map(str, self.cards)))

    '''
    Every Hand Type returns the cards that make up the game if it is present and None otherwise
    '''
    @property
    def flush(self):
        if len(self.ranks) == 1:
            return [(self.cards)]
        return []
    
    @property
    def straight(self):
        if list(sorted(self.ranks)) == range(min(self.ranks), max(self.ranks) + 1):
            return [(self.cards)]
        return []

    @property
    def straight_flush(self):
        if self.flush and self.straight:
            return [(self.cards)]
        return []

    @property
    def game(self):
        four_of_a_kind = self.groups[4]
        three_of_a_kind = self.groups[3]
        pairs = self.groups[2]
        busted = self.groups[1]
        if self.straight_flush:
            return 'Straight Flush' ,self.straight_flush
        if four_of_a_kind:
            return 'Four of a Kind', four_of_a_kind
        elif three_of_a_kind and pairs:
            return 'Full House', three_of_a_kind.update(paris)
        elif self.flush:
            return 'Flush', self.flush
        elif self.straight:
            return 'Straight', self.straight
        elif three_of_a_kind:
            return 'Three of a Kind', three_of_a_kind
        elif len(pairs) == 2:
            return 'Double Pair', pairs
        elif len(pairs) == 1:
            return 'Pair', pairs
        else:
            return 'Busted', busted



def main():
    deck = Deck()
    hand = deck.random_hand(5)
    print(hand)
    name, game = hand.game
    print(f'You have got a {name}')
    for g in game:
        print(list(map(str, g)))

if __name__ == '__main__':
    main()