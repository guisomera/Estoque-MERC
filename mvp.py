import pandas as pd 
from defs import ordenar, ingest

choose_order, choose_filter = 0, 0


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

#Transforma todos os numeros da tabela em inteiros e troca NaN por 0 
wide = wide.fillna(0).astype(int)

#Opçoes para filtrar a tabela 
print("Filtros")
print("1- Total\n" \
      "2- Entrada\n" \
      "3 - Saida\n")

print("Ordem - \n"
      "1- Crescente\n" \
      "2- Decrescente\n")

#Escolha do usuario
choose_filter = int(input("Escolha o filtro"))
choose_order  = int(input("Escolha a ordem"))

#Lógica da escolha
if 0 < choose_filter < 4:
    if choose_filter == 1:
        coluna = "Total"
    elif choose_filter == 2:
        coluna = "Entrada"
    else:
        coluna = "Saida"

if 0 < choose_order < 3:
    crescente = True if choose_order == 1 else False

#Chama a função pra ordenar
wide = ordenar(wide, coluna, crescente)

print(wide.head(10))



