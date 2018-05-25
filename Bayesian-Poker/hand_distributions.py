import itertools

class Card():
    suits = { 'Hearts': '♥', 'Spades': '♣', 'Clubs': '♠', 'Diamonds': '♦'}
    ranks = dict(zip(range(1, 14), '123456789JQKA'))
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return Card.ranks[self.rank] + Card.suits[self.suit]

# deck = list(itertools.product(ranks, suits))



def main():
    print(Card(13, 'Hearts'))

if __name__ == '__main__':
    main()