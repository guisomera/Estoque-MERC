import pandas as pd
import streamlit as st

st.title("ESTOQUE MERCÚRIO")
df = st.session_state.get("final_df")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7, gap="small")
result = None

if df is None:
    st.info("Sem dados! Volte para a página inicial e insira os dados")
    st.stop()

df = pd.DataFrame(df, columns=["Estoque"])

filtros = {
    "Nenhum": lambda df : None,
    "Itens em estoque": lambda df: df[df["Estoque"] > 0],
    "Itens faltantes": lambda df: df[df["Estoque"] < 1],
    "Abaixo do Mínimo": lambda df: df[df["Estoque"]]
}

filtro_selecionado = st.selectbox("Escolha um filtro", filtros, index= 0)
if filtro_selecionado == "Nenhum":
    st.info("Selecione um filtro")
    st.stop()
else:
    df_filtered = filtros[filtro_selecionado](df)
    st.write(df_filtered)