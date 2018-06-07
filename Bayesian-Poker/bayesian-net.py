from pomegranate import *
import pandas as pd

sheets = [
    ('Round', [], list(range(4))),
    ('Board', ['Round', 'OPP_current'], list(range(1, 18))),
    ('BPP_current', ['Round', 'BPP_final'], list(range(1, 18))),
    ('OPP_current', ['Round', 'OPP_final'], list(range(1, 18))),
    ('BPP_final', [], list(range(1, 18))),
    ('OPP_final', ['BPP_final'], list(range(1, 18))),
    ('BPP_win', ['BPP_final', 'OPP_final'], [0, 1]),
    ]

nodes = [name for name, _, _ in sheets]

def get_metadata_of(node):
    return list(filter(lambda s: s[0] == node, sheets))[0]

def build_path_to(node):
    return f'./experiment-results/2M-split/Pome/{node}.csv'

dfs = [(node, pd.read_csv(build_path_to(node))) for node in nodes]

cpts = dict()
for node, df in dfs:
    _, parents, values = get_metadata_of(node)
    if not any(parents):
        # if we have only two columns, DiscreteDistribution
        cpts[node] = DiscreteDistribution(dict(df.as_matrix()))
    else:
        pass

print(cpts)
