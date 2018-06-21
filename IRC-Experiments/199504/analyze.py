"""
Each database contains:
- `Hands`: a file 'hdb' which summarizes each hand in a single line
- `Rosters`: a file 'hroster' that records the list of players dealt in on each hand
- `Actions`: a file 'pdb.[name]' for each player that summarizes that player's actions during each hand.

The corresponding lines in each file all have the same 'timestamp'
"""

import pandas as pd

hands_headers = ('timestamp', 'game_set#', 'game#', 'nb_players',
                 'nb_flop', 'pot_flop', 'nb_turn', 'pot_turn',
                 'nb_river', 'pot_river', 'nb_showdown', 'pot_showdown', 'board')

rosters_headers = ('timestamp', 'nb_players', 'players')

actions_names = ('player', 'timestamp', 'nb_players', 'first_player', 'preflop', 'flop', 'turn', 'river', 
                 'bankroll', 'total_action', 'pot_won', 'cards')

hands = pd.read_csv('Results/hdb.csv', names=hands_headers).set_index('timestamp')
rosters = pd.read_csv('Results/hroster.csv', skipinitialspace=True, quotechar='"', names=rosters_headers).set_index('timestamp')
actions = pd.read_csv('Results/pdb.csv', skipinitialspace=True, quotechar='"', names=actions_names)

## join hands and rosters, dropping duplicate column: nb_players
rosters = rosters.drop(['nb_players'], axis=1)
rosters = rosters.join(hands)


print(rosters)
