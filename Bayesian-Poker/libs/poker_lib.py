import itertools
import random
import collections

class Deck():
    suits = { 'Hearts': 'h', 'Spades': 's', 'Clubs': 'c', 'Diamonds': 'd'}
    ranks = {i: str(i) for i in range(2, 10)}
    ranks.update({10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'})

    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in itertools.product(self.ranks, self.suits)]
    
    def __str__(self):
        return str(list(map(str, self.cards)))

    def random_hand(self, size):
        return Hand(random.sample(self.cards, size))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, amount):
        return [self.cards.pop() for _ in range(amount)]

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
        # group cards by rank
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
        if len(self.suits) == 1:
            return [(self.cards)]
        return []
    
    @property
    def straight(self):
        if len(self.ranks) == self.size and \
            list(sorted(self.ranks)) == list(range(min(self.ranks), max(self.ranks) + 1)):
            return [(self.cards)]
        return []

    @property
    def straight_flush(self):
        if self.flush and self.straight:
            return [(self.cards)]
        return []

    @property
    def game(self):
        # returns a list of tuples containing the goups relevant to the game
        # i.e a hand with a pair would return [(Ah, Ad), (2s, 2c)]
        four_of_a_kind = self.groups[4]
        three_of_a_kind = self.groups[3]
        pairs = self.groups[2]
        busted = self.groups[1]
        if self.straight_flush:
            return 'Straight Flush' ,self.straight_flush, 16
        if four_of_a_kind:
            return 'Four of a Kind', four_of_a_kind, 15
        elif three_of_a_kind and pairs:
            return 'Full House', three_of_a_kind.extend(pairs), 14
        elif self.flush:
            return 'Flush', self.flush, 13
        elif self.straight:
            return 'Straight', self.straight, 12
        elif three_of_a_kind:
            return 'Three of a Kind', three_of_a_kind, 11
        elif len(pairs) == 2:
            return 'Double Pair', pairs, 10
        elif len(pairs) == 1:
            return 'Pair', pairs, 9
        else:
            return 'Busted', busted, 4

    @property
    def hand_type(self):
        hand_game, game_groups, hand_number = self.game
        if hand_game == 'Busted':
            highest_card = Card.highest([card for group in game_groups for card in group])
            print(highest_card)
        elif hand_game == 'Pair':
            highest_card = game_groups[0][0]
            print(highest_card)
        return hand_number

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