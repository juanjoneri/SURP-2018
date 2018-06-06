import pandas as pd


def import_xls(path, sheets):
    xls = pd.ExcelFile(path)
    dataframes = []
    for sheet in sheets:
        dataframes.append(pd.read_excel(xls, sheet))

    return dataframes

if __name__ == '__main__':
    path = './experiments-results/2M-split/results-clean.xlsx'
    sheets = ['Round', 'Board']
    dfs = import_xls(path, sheets)
    for df in dfs:
        print(df)
