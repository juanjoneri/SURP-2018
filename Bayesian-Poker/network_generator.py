from libs.deuces import Deck, Card, Evaluator

headers = ['BPP_win', 'BPP_final', 'OPP_final', 'BPP_current', 'OPP_current', 'round', 'board']

hand_types = [
    'busted-low',
    'busted-medium',
    'busted-queen',
    'busted-king',
    'busted-ace',
    'pair-low',
    'pair-medium',
    'pair-queen',
    'pair-king',
    'pair-ace',
    'doble-pair',
    'three-of-a-kind',
    'straight',
    'flush',
    'full-house',
    'four-of-a-kind',
    'straight-flush'
]

score_ranges = {'busted': (7462,), 'pair': (1,)}

def refine_score(score):
    score_class = evaluator.get_rank_class(score)
    
    # high card
    if score_class == 8:
        print(score)
    # pair
    elif score_class == 9:
        print(score)
    
    return score_class

evaluator = Evaluator()

def get_score(hand, board=[]):
    return evaluator.get_rank_class(evaluator.evaluate(hand, board))


def main():
    deck = Deck()

    BPP = deck.draw(2)
    OPP = deck.draw(2)

    board = deck.draw(5)

    print('\nBPP')
    Card.print_pretty_cards(BPP)

    print('\nOPP')
    Card.print_pretty_cards(OPP)

    print('\nBoard')
    Card.print_pretty_cards(board)

    ## PRE-FLOP
    print('\npre-flop')
    BPP_current = get_score(BPP)
    print(BPP_current)
    OPP_current = get_score(OPP)
    print(OPP_current)

    ## FLOP
    print('\nflop')
    BPP_current = get_score(BPP, board[:4])
    print(BPP_current)
    OPP_current = get_score(OPP, board[:4])
    print(OPP_current)

    ## TURN
    print('\nflop')
    BPP_current = get_score(BPP, board[:5])
    print(BPP_current)
    OPP_current = get_score(OPP, board[:5])
    print(OPP_current)

    ## RIVER
    print('\nflop')
    BPP_current = get_score(BPP, board)
    print(BPP_current)
    OPP_current = get_score(OPP, board)
    print(OPP_current)

    BPP_win = evaluator.evaluate(board, BPP) < evaluator.evaluate(board, OPP)
    print('win' if BPP_win else 'lost')

if __name__ == '__main__':
    main()