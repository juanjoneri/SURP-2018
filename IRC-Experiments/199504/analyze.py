"""
Each database contains:
- `Hands`: a file 'hdb' which summarizes each hand in a single line
- `Roster`: a file 'hroster' that records the list of players dealt in on each hand
- `Actions`: a file 'pdb.[name]' for each player that summarizes that player's actions during each hand.

The corresponding lines in each file all have the same 'timestamp'
"""

# HANDS
# convert hands csv             $ sed -i -E "s/\([0-9]\) /\1, /g" test.txt
# split the flop, turn, etc     $ sed -i -E "s/\//, /g" pdb

# ROSTER
# convert roster csv            $ sed -i -E "s/\([0-9A-Za-z]\) /\1, /g" test.txt

# ACTIONS
# concat all pdb files          $ cat pdb/pdb.* >> pdb.all.csv 

import pandas as pd

# flop, turn, etc show nb_players/starting_pot
hands_headers = ('timestamp', 'game_set#', 'game#', 
                 'nb_players', 'flop', 'turn', 'river', 'showdown', 'board')

roster_headers = ('')


hands = pd.read_csv('./hdb', names=hands_headers)
print(hands.head())

'''

- country with best steak
- what makes a good sushi
- best netflix series to watch during summer 2018
- ipad pro vs ipad