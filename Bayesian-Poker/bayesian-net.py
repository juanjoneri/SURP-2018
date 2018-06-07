from pomegranate import DiscreteDistribution, ConditionalProbabilityTable, State, BayesianNetwork
import pandas as pd

## parents first!
sheets = [
    ('Round', [], list(range(4))),
    ('BPP_final', [], list(range(1, 18))),
    ('BPP_current', ['Round', 'BPP_final'], list(range(1, 18))),
    ('OPP_final', ['BPP_final'], list(range(1, 18))),
    ('OPP_current', ['Round', 'OPP_final'], list(range(1, 18))),
    ('Board', ['Round', 'OPP_current'], list(range(1, 18))),
    ('BPP_win', ['BPP_final', 'OPP_final'], [0, 1]),
    ]


def get_metadata_of(node):
    # returns information about parents, and discrete values
    return list(filter(lambda s: s[0] == node, sheets))[0]

def build_path_to(node):
    # returns a path to that node: breakable!
    return f'./experiment-results/2M-split/Pome/{node}.csv'

nodes = [name for name, _, _ in sheets]
dfs = [(node, pd.read_csv(build_path_to(node))) for node in nodes]

def build_cpts(dfs):
    cpts = dict() # maps the name of the node to its cpt
    for node, df in dfs:
        _, parents, values = get_metadata_of(node)
        if not any(parents):
            # if we have only two columns, DiscreteDistribution
            cpts[node] = DiscreteDistribution(dict(df.values))
        else:
            cpts[node] = ConditionalProbabilityTable(df.values, [cpts[parent] for parent in parents])

    return cpts

def build_net(cpts):
    states = dict()
    for name, cpt in cpts.items():
        states[name] = State(cpt, name=name)

    model = BayesianNetwork('Poker Game')
    model.add_states(*list(states.values()))

    for name, parents, _ in sheets:
        for parent in parents:
            print(states[parent])
            model.add_transition(states[parent], states[name])

    model.bake()
    return model

if __name__ == '__main__':
    cpts = build_cpts(dfs)
    model = build_net(cpts)
    print(model.predict_proba({'BPP_win': 1, 'BPP_current': 5, 'Round': 0, 'Board': 1})[-1])
