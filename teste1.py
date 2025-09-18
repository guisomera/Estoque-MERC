import pandas as pd 


data = pd.read_csv("relatorio.csv", sep=";", encoding="utf-8")              #Le e armazena o csv

df= pd.DataFrame(data, columns=['Produto', 'Evento', 'Quantidade'])         #Armazena apenas as colunas produtos, evento e quantidade do csv

df = df.replace({
    "Evento": {                                                             #Tratando dados
        "TransferenciaEntrada": "Entrada",
        "TransferenciaSaida": "Saida"
    }
})

#Agrupa os dados, deixando cada produto com apenas 2 linhas, uma com saida e entrada 
agg = df.groupby(["Produto", "Evento"])["Quantidade"].sum().reset_index()  

wide = agg.pivot_table(       #Olha linha por linha. do agg
    index='Produto',          #Define quem sera a linha da tabela, nesse caso, os produtos (1 linha por produto)
    columns="Evento",         #Pega os valores da colua evento e cria uma coluna separada pra cada 
    values="Quantidade",      #Pega os valores da coluna quantidade
    aggfunc="sum"             #Se houver mais de uma linha pro mesmo produto (varias entradas) ele soma
)

wide['Total'] = wide['Entrada'] - wide['Saida']
#Transforma todos os numeros da tabela em inteiros, troca NaN por 0 e coloca em ordem crescente de saida 
wide = wide.fillna(0).astype(int).sort_values(by='Saida', ascending=False)  

print(wide.head())

