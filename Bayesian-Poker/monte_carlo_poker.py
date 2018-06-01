from libs.deuces import Deck, Card, Evaluator

headers = ['BPP_win', 'BPP_final', 'OPP_final', 'BPP_current', 'OPP_current', 'round', 'board']

evaluator = Evaluator()

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

# perhaps make deuces handle any size of hand?
worst_representative = [
    [Card.new('2h'), Card.new('3h')],
    [Card.new('2h'), Card.new('9h')],
    [Card.new('2h'), Card.new('Qh')],
    [Card.new('2h'), Card.new('Kh')],
    [Card.new('2h'), Card.new('Ah')],
    \
    [Card.new('3d'), Card.new('3h')],
    [Card.new('9d'), Card.new('9h')],
    [Card.new('Qd'), Card.new('Qh')],
    [Card.new('Kd'), Card.new('Kh')],
    [Card.new('Ad'), Card.new('Ah')],
    \
    [Card.new('2d'), Card.new('2h'), Card.new('3d'), Card.new('3h'), Card.new('4h')],
    \
    [Card.new('2d'), Card.new('2h'), Card.new('2c'), Card.new('3h'), Card.new('4h')],
    \
    [Card.new('Ad'), Card.new('2h'), Card.new('3c'), Card.new('4h'), Card.new('5h')],
    \
    [Card.new('2d'), Card.new('3d'), Card.new('4d'), Card.new('5d'), Card.new('7d')],
    \
    [Card.new('2d'), Card.new('2h'), Card.new('2c'), Card.new('3h'), Card.new('3h')],
    \
    [Card.new('2d'), Card.new('2h'), Card.new('2c'), Card.new('2s'), Card.new('3h')],
    \
    [Card.new('Ah'), Card.new('2h'), Card.new('3h'), Card.new('4h'), Card.new('5h')]
]

score_ranges = dict(zip(map(lambda h: evaluator.evaluate(h), worst_representative) , hand_types))

print(score_ranges)

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

def game():
    deck = Deck()
    board = deck.draw(5)
    player1_hand = deck.draw(2)
    player2_hand = deck.draw(2)

    Card.print_pretty_cards(board)
    Card.print_pretty_cards(player1_hand)
    Card.print_pretty_cards(player2_hand)

    hands = [player1_hand, player2_hand]
    evaluator.hand_summary(board, hands)



if __name__ == '__main__':
    #main()
    #game()
    for k, v in score_ranges.items():
        print(k, v)