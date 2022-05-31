#pandasfiles.py
import pandas as pd

url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS1o93qTAt7aBFyROYMLs0sAsxrhY4wwH2yABkV_wpNk6rsfY847EMFLDmZz8TVPIJKunU2G8YQkev5/pub?gid=0&single=true&output=csv'

def importa_planilha(colunas):
    df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
    # dd = df.to_dict('index')
    # print(df)
    # print(dd)
    return df.to_dict('index')

#importa_planilha('id')
    #df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)