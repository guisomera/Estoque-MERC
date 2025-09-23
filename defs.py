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

    df_clean = df.replace({                                                   #Tratando dados
        "Evento":{
            "TransferenciaSaida": "Saida", 
            "TransferenciaEntrada": "Entrada"
        }
    })

    df_clean["Quantidade"] = pd.to_numeric(df_clean["Quantidade"], errors="coerce").fillna(0)

    #Junta as linhas que tem mesmo produto e evento
    #Soma as quantidades
    #volta pro formato normal
    agg_products_events = df_clean.groupby(["Produto", "Evento"])["Quantidade"].sum().reset_index()  

    wide = agg_products_events.pivot_table(         #Percorre linha por linha 
        index= 'Produto',               #Define quem sera a linha
        columns= 'Evento',              #Pega os valores da coluna evento e cria uma coluna separada pra cada
        values= 'Quantidade',            #Pega os valores da coluna quantidade
        aggfunc='sum'                   #Se tiver mais de uma linha no mesmo produto (duas entradas) ele soma
    )

    wide = wide.fillna(0).astype(int)           #Transforma os NaN em 0
    wide = wide.reindex(columns=["Entrada", "Saida"], fill_value= 0 )
    wide['Total'] = wide['Entrada'] - wide['Saida']     #Cria a coluna total

    return wide