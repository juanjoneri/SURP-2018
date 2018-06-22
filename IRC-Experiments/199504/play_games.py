import pandas as pd
    

headers = [
        'timestamp', 'players', 'pot_flop', 'pot_turn', 'pot_river', 'pot_showdown', 
        'board', 'player', 'first_player', 'preflop', 'flop', 'turn', 'river', 'bankroll', 
        'total_action', 'pot_won', 'cards',
        ]

from deuces import Deck, Card, Evaluator

class TexasPlayer():
    ACTIONS = dict(zip('Bcfrkb', ('blind', 'call', 'fold', 'raise', 'check', 'bet')))

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
    def __init__(self, p1, p2, df_row):
        self.board = [Card.new(value) for value in df_row['board'].item().strip().split(' ')]
        self.players = (p1, p2) if int(df_row['first_player'].item()) == 1 else (p2, p1)

    def __str__(self):
        return f'{self.players[0]} vs {self.players[1]}'

if __name__ == '__main__':
    df = pd.read_pickle('Results/dataframe.pkl')
    rows, cols = df.shape
 
    print(df.head(10))
    for i in range(0, 10, 2):
        row1, row2 = df.loc[[i]], df.loc[[i+1]]
        p1 = TexasPlayer(row1)
        p2 = TexasPlayer(row2)
        game = TexasGame(p1, p2, row1)
        print(game)