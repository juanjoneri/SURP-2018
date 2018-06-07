import pandas as pd

def order_key(col):
    # order columns for use in BN, with parent node first
    if type(col) is int:
        return col
    else:
        return 0


def import_xls(path, sheets, missing_data='￯﾿ﾽ', epsilon=0.00005):
    # improt poker data as exported by tetrad
    xls = pd.ExcelFile(path)
    dataframes = []
    for name, parents, values in sheets:
        df = pd.read_excel(xls, name)
        df = df.replace(missing_data, epsilon)
        pome_df = pd.DataFrame(columns=[*parents, name, 'P'])
        for _, row in df.iterrows():
            for value in values:
                p_value = row[value]
                parent_values = row[parents]
                new_row = {'P': p_value, name: value}
                new_row.update(parent_values)
                pome_df = pome_df.append(new_row, ignore_index=True)
        dataframes.append(pome_df)

    return dataframes

if __name__ == '__main__':
    path = './experiments-results/2M-split/results-clean.xlsx'
    #   (Name, *Parents, *Values)
    sheets = [
        ('Round', [], list(range(4))),
        ('Board', ['Round', 'OPP_current'], list(range(1, 18))),
        ('BPP_current', ['Round', 'BPP_final'], list(range(1, 18))),
        ('OPP_current', ['Round', 'OPP_final'], list(range(1, 18))),
        ('BPP_final', [], list(range(1, 18))),
        ('OPP_final', ['BPP_final'], list(range(1, 18))),
        ('BPP_win', ['BPP_final', 'OPP_final'], [0, 1]),
        ]

    dfs = import_xls(path, sheets)

    for df in dfs:
        print(df.head())
