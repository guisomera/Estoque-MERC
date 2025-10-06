import pandas as pd 

def ordenar(df, coluna, crescente=True):
    return df.sort_values(by=coluna, ascending=crescente)

def ingest(files: list):
    data = []
    for csv in files:
        df = pd.read_csv(csv, sep=None, engine="python", encoding="utf-8-sig")
        data.append(df)

    return pd.concat(data, ignore_index=True)       #Junta tudo em um documento só

def treatments(raw_data):
    df = pd.DataFrame(raw_data, columns=['Produto', 'Evento', 'Quantidade'])  #Armazena só os dados que quero

    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0)

    #Junta as linhas que tem mesmo produto e evento
    #Soma as quantidades
    #volta pro formato normal
    agg_products_events = df.groupby(["Produto", "Evento"])["Quantidade"].sum().reset_index()  

    wide = agg_products_events.pivot_table(         #Percorre linha por linha 
        index= 'Produto',               #Define quem sera a linha
        columns= 'Evento',              #Pega os valores da coluna evento e cria uma coluna separada pra cada
        values= 'Quantidade',            #Pega os valores da coluna quantidade
        aggfunc='sum'                   #Se tiver mais de uma linha no mesmo produto (duas entradas) ele soma
    )

    wide = wide.fillna(0).astype(int)           #Transforma os NaN em 0
    wide = wide.reindex(columns=["Entrada", "Saida"], fill_value= 0 )
    wide['Estoque'] = wide['Entrada'] - wide['Saida']     #Cria a coluna total

    return wide

def concat_treaments(concated_df):
    final_df = pd.DataFrame(concated_df)
    final_df = final_df[["Entrada", "Saida", "Estoque"]].astype(int)
    final_df.index.name = 'Produto'

    return final_df

def get_balance(raw_data):
    #Fiz outro dataframe por conta da estrutura do grafico de pizza
    df = pd.DataFrame(raw_data, columns=["Entrada", "Saida"])
    total_entrada = df["Entrada"].sum()
    total_saida = df["Saida"].sum()

    sum_balance = pd.DataFrame({"Categoria": ["Entrada", "Saida", "Estoque"], "Valor": [total_entrada, total_saida, total_entrada - total_saida]}, index=["Entrada", "Saida", "Saldo"])

    return sum_balance