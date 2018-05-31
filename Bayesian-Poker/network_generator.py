from libs.poker_lib import Deck, Hand
import random

headers = ['BPP_win', 'BPP_final', 'OPP_final', 'BPP_current', 'OPP_current', 'round', 'board']

def stringify(list_of_cards):
    return str(list(map(str, list_of_cards)))

def main():
    deck = Deck()
    deck.shuffle()

    h1, h2 = deck.deal(2), deck.deal(2)
    
    flop = deck.deal(3)
    turn = flop + deck.deal(1)
    river = turn + deck.deal(1)

    board_states = Hand([]), Hand(flop), Hand(turn), Hand(river)

    print('boards states', stringify(board_states))
    
    BPP = Hand(h1), Hand(flop + h1), Hand(turn + h1), Hand(river + h1)
    OPP = Hand(h2), Hand(flop + h2), Hand(turn + h2), Hand(river + h2)

    print('BPP', stringify(BPP))
    print('OPP', stringify(OPP))

if __name__ == '__main__':
    main()