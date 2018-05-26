from poker_lib import Deck
import collections

deck = Deck()

def check_probabilities(sample_size):
    games = collections.defaultdict(int)
    for _ in range(sample_size):
        hand = deck.random_hand(5)
        games[hand.game[0]] += 1

    for g, i in games.items():
        print(g, f'{100*i/sample_size}%')

def main():
    # hand = deck.random_hand(2)
    # print(hand)
    # print(hand.ranks)
    # print(hand.straight)
    
    check_probabilities(1000)

    

if __name__ == '__main__':
    main()