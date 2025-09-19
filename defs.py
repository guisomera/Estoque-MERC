import pandas as pd 

def ordenar(df, coluna, crescente=True):
    return df.sort_values(by=coluna, ascending=crescente)