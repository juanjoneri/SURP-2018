from libs.poker_lib import Deck, Hand
import random

headers = ['BPP_win', 'BPP_final', 'OPP_final', 'BPP_current', 'OPP_current', 'round', 'board']
hand_types = {
    0: 'busted-low',
    1: 'busted-medium',
    2: 'busted-queen',
    3: 'busted-king',
    4: 'busted-ace',
    5: 'pair-low',
    6: 'pair-medium',
    7: 'pair-queen',
    8: 'pair-king',
    9: 'pair-ace',
    10: 'Double Pair',
    11: 'Three of a Kind',
    12: 'Straight',
    13: 'Flush',
    14: 'Full House',
    15: 'Four of a Kind',
    16: 'Straight Flush'
}


def stringify(list_of_cards):
    return str(list(map(str, list_of_cards)))

def main():
    deck = Deck()
    deck.shuffle()

    h1, h2 = deck.deal(2), deck.deal(2)
    
    flop = deck.deal(3)
    turn = flop + deck.deal(1)
    river = turn + deck.deal(1)

    rounds = tuple(range(4))
    board_states = Hand([]), Hand(flop), Hand(turn), Hand(river)

    print('boards states', stringify(board_states))
    
    BPP = Hand(h1), Hand(flop + h1), Hand(turn + h1), Hand(river + h1)
    BPP_games = tuple(map(lambda h: h.hand_type, BPP))
    
    OPP = Hand(h2), Hand(flop + h2), Hand(turn + h2), Hand(river + h2)
    OPP_games = tuple(map(lambda h: h.hand_type, OPP))

    print('\nBayesian Poker Player')
    print('BPP', stringify(BPP))
    print('BPP games', BPP_games)

    print('\nOpponent')
    print('OPP', stringify(OPP))
    print('OPP games', OPP_games)

    # TURN INTO STATICMETHOD IN HAND
    BPP_win = BPP_games[-1] > OPP_games[-1]
    print('\nResults')
    print(BPP_win)

if __name__ == '__main__':
    main()