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

"""
column 1        player nickname
column 2        timestamp of this hand (see HDB)
column 3        number of player dealt cards
column 4        position of player (starting at 1, in order of cards received)
column 5        betting action preflop (see below)
column 6        betting action on flop (see below)
column 7        betting action on turn (see below)
column 8        betting action on river (see below)
column 9        player's bankroll at start of hand
column 10       total action of player during hand
column 11       amount of pot won by player
column 12+      pocket cards of player (if revealed at showdown)
"""

hands = pd.read_csv('Results/hdb.csv', names=hands_headers)
rosters = pd.read_csv('Results/hroster.csv', skipinitialspace=True, quotechar='"', names=roster_headers)
actions = pd.read_csv('Results/pdb.csv', skipinitialspace=True, quotechar='"', names=actions_names)

print(actions)
