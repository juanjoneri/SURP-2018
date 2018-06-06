import pandas as pd

def order_key(col):
    # order columns for use in BN, with parent node first
    if type(col) is int:
        return col
    else:
        return 0


def import_xls(path, sheets, missing_data='￯﾿ﾽ'):
    # improt poker data as exported by tetrad
    xls = pd.ExcelFile(path)
    dataframes = []
    for sheet in sheets:
        df = pd.read_excel(xls, sheet)
        df = df.replace(missing_data, 0)
        df = df.reindex_axis(sorted(df.columns, key=order_key), axis=1)
        dataframes.append(df)

    return dataframes

if __name__ == '__main__':
    path = './experiments-results/2M-split/results-clean.xlsx'
    sheets = ['Round', 'Board', 'BPP_current', 'OPP_current', \
              'BPP_final', 'OPP_final', 'BPP_win']

    dfs = import_xls(path, sheets)

    OPP_final = dfs[-2]
    print(OPP_final[1][OPP_final['BPP_final'] == 10])

    OPP_current = dfs[3]
    print(OPP_current)
