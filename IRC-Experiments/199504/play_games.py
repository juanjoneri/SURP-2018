import pandas as pd
    

headers = [
        'timestamp', 'players', 'pot_flop', 'pot_turn', 'pot_river', 'pot_showdown', 
        'board', 'player', 'first_player', 'preflop', 'flop', 'turn', 'river', 'bankroll', 
        'total_action', 'pot_won', 'cards',
        ]


class TexasPlayer():
    def __init__(self, df_row):
        pass

class TexasGame():
    def __init__(self, player1, player2, df_row):
        self.board = df_row['board'].item().strip().split(' ')
        self.players = df_row['players'].item().split(',')

    def __str__(self):
        return str(self.board)

if __name__ == '__main__':
    df = pd.read_pickle('Results/dataframe.pkl')
    rows, cols = df.shape
 
    for i in range(0, 10, 2):
        player1, player2 = df.loc[[i]], df.loc[[i+1]]
        game = TexasGame(player1, player2, player1)
        print(game)