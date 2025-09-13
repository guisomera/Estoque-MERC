import pandas as pd 
import pandas as pd

data = pd.read_csv("Relatorio.csv", sep=";", encoding="utf-8")

df= pd.DataFrame(data, columns=['Produto', 'Evento', 'Quantidade'])

new_df = df.replace({
    "Evento": {
        "TransferenciaEntrada": "Entrada",
        "TransferenciaSaida": "Saida"
    }
})

agrupado = new_df.groupby(["Produto", "Evento"])["Quantidade"].sum().reset_index()

print(agrupado)
print(new_df["Evento"].unique())