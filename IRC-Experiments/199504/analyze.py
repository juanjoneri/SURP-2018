"""
Each database contains:
- `Hands`: a file 'hdb' which summarizes each hand in a single line
- `Roster`: a file 'hroster' that records the list of players dealt in on each hand
- `Actions`: a file 'pdb.[name]' for each player that summarizes that player's actions during each hand.

The corresponding lines in each file all have the same 'timestamp'
"""

import pandas as pd

# flop, turn, etc show nb_players/starting_pot
hands_headers = ('timestamp', 'game_set#', 'game#', 'nb_players', 
                 'nb_flop', 'pot_flop', 'nb_turn', 'pot_turn', 
                 'nb_river', 'pot_river', 'nb_showdown', 'pot_showdown', 'board')

roster_headers = ('timestamp', 'nb_players', 'players')


hands = pd.read_csv('Results/hdb.csv', names=hands_headers)
print(hands.head())
