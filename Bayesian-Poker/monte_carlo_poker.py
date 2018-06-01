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
worst_scores = list(map(lambda h: evaluator.evaluate(h), worst_representative))

score_ranges = dict(zip(worst_scores , hand_types))
hand_values = dict(zip(hand_types, range(1, 18))) # high values mean better games

def get_score(hand, board=[]):
    value = evaluator.evaluate(hand, board)
    worst_hands = list(filter(lambda v: v >= value, score_ranges))
    return hand_values[score_ranges[min(worst_hands)]]

def play_poker():
    deck = Deck()

    BPP = deck.draw(2)
    OPP = deck.draw(2)

    board = deck.draw(5)
    board_score = get_score(board)

    ## RIVER
    BPP_final = get_score(BPP, board)
    OPP_final = get_score(OPP, board)

    BPP_win = 1 if evaluator.evaluate(board, BPP) < evaluator.evaluate(board, OPP) else 0

    for r in range(4):
        if r == 0:
            BPP_current = get_score(BPP)
            OPP_current = get_score(OPP)
        else:
            BPP_current = get_score(BPP, board[:3+r])
            OPP_current = get_score(OPP, board[:3+r])
        
        print(r, board_score, BPP_current, OPP_current, BPP_final, OPP_final, BPP_win, sep=', ')


if __name__ == '__main__':
    print(*headers, sep=', ')
    for _ in range(100000):
        play_poker()