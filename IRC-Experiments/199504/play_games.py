import pandas as pd
    

headers = [
        'timestamp', 'players', 'pot_flop', 'pot_turn', 'pot_river', 'pot_showdown', 
        'board', 'player', 'first_player', 'preflop', 'flop', 'turn', 'river', 'bankroll', 
        'total_action', 'pot_won', 'cards',
        ]

from deuces import Deck, Card, Evaluator
from itertools import zip_longest

class TexasPlayer():
    def __init__(self, df_row):
        self.name = df_row['player'].item()
        self.pot_won = int(df_row['pot_won'].item())
        self.cards = [Card.new(value) for value in df_row['cards'].item().split(', ')]

        self.actions = [
            df_row['preflop'].item(),
            df_row['flop'].item(),
            df_row['turn'].item(),
            df_row['river'].item(),
            ]

    def __str__(self):
        return self.name

    @property
    def won(self):
        return self.pot_won > 0

class TexasGame():
    ACTIONS = dict(zip('Bcfrkb', ('pays blind', 'calls', 'folds', 'raises', 'checks', 'bets')))

    def __init__(self, p1, p2, df_row):
        self.board = [Card.new(value) for value in df_row['board'].item().strip().split(' ')]
        self.pot = [
            0,
            int(df_row['pot_flop'].item()),
            int(df_row['pot_turn'].item()),
            int(df_row['pot_river'].item()),
            int(df_row['pot_showdown'].item()),
        ]
        self.players = (p1, p2) if int(df_row['first_player'].item()) == 1 else (p2, p1)

    def __str__(self):
        return f'{self.players[0]} vs {self.players[1]}'

    @property
    def winner(self):
        p1, p2 = self.players
        return p1 if p1.won else p2 

    @property
    def simmulate(self):
        p1, p2 = self.players
        for i, stage in enumerate(('PREFLOP', 'FLOP', 'TURN', 'RIVER')):
            print(f'----{stage}----')
            print(f'The pot is currently at: ${self.pot[i]}')
            if stage is 'PREFLOP':
                print(f'{p1} draws: ', end='')
                Card.print_pretty_cards(p1.cards)
                print(f'{p2} draws: ', end='')
                Card.print_pretty_cards(p2.cards)
            else:
                print('The board is currently: ', end='')
                Card.print_pretty_cards(self.board[:2+i])
                

            for a1, a2 in zip_longest(p1.actions[i], p2.actions[i]):
                if a1 is not None:
                    print(f'> {p1.name} {TexasGame.ACTIONS[a1]}')
                if a2 is not None:
                    print(f'> {p2.name} {TexasGame.ACTIONS[a2]}')
                if a1 == 'f' or a2 == 'f':
                    break

        print('----Results----')
        print(f'{self.winner.name} wins ${self.winner.pot_won}!\n')


if __name__ == '__main__':
    df = pd.read_pickle('Results/dataframe.pkl')
    rows, cols = df.shape
 
    print(df.head(10))
    for i in range(0, 4, 2):
        row1, row2 = df.loc[[i]], df.loc[[i+1]]
        p1 = TexasPlayer(row1)
        p2 = TexasPlayer(row2)
        game = TexasGame(p1, p2, row1)
        game.simmulate