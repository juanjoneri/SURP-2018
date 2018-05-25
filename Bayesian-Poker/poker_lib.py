import itertools
import random
import collections

class Card():
    suits = { 'Hearts': '♥', 'Spades': '♣', 'Clubs': '♠', 'Diamonds': '♦'}
    ranks = {i: str(i) for i in range(2, 11)}
    ranks.update({11: 'J', 12: 'Q', 13: 'K', 14: 'A'})
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return Card.ranks[self.rank] + Card.suits[self.suit]

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
    size = 5
    def __init__(self, cards):
        if len(cards) != Hand.size:
            raise IndexError(f'Hands must be composed of {Hand.size} Cards')
        
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
            return self.cards
        return []
    
    @property
    def straight(self):
        if list(sorted(self.ranks)) == range(min(self.ranks), max(self.ranks) + 1):
            return self.cards
        return []

    @property
    def straight_flush(self):
        if self.flush and self.straight:
            return self.cards
        return []

    @property
    def best_group(self):
        four_of_a_kind = self.groups[4]
        three_of_a_kind = self.groups[3]
        pairs = self.groups[2]
        busted = self.groups[1]
        if four_of_a_kind:
            return four_of_a_kind
        elif three_of_a_kind and pairs:
            return three_of_a_kind.update(paris)
        elif three_of_a_kind:
            return three_of_a_kind
        elif pairs:
            return pairs
        else:
            return busted


deck = [Card(rank, suit) for rank, suit in itertools.product(Card.ranks, Card.suits)]

def main():
    hand = Hand(random.sample(deck, 5))
    print(len(deck))
    print(hand)
    print(hand.best_group)
    # print(Card.highest(hand.cards))
    # print(hand.suits)
    # print(hand.ranks)
    # print(hand.busted)

if __name__ == '__main__':
    main()