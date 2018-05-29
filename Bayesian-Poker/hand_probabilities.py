from poker_lib import Deck, Card, Hand
import collections

deck = Deck()

def check_probabilities(sample_size):
    games = collections.defaultdict(int)
    for _ in range(sample_size):
        hand = deck.random_hand(5)
        games[hand.game[0]] += 1

    cummulative = 0
    for g, i in sorted(games.items(), key=lambda x: x[1]):
        probability = 100*i/sample_size
        cummulative += probability
        print(f'{g:15} | {probability:5}% | {cummulative:5}%')

def main():
    check_probabilities(10000)

    

if __name__ == '__main__':
    main()