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

positive = df["Estoque"] > 0
negaitve = df["Estoque"] < 1

if "show_mode" not in st.session_state:
    st.session_state["show_mode"] = "nenhum"

with col1:
    positive_button = st.button("Mostrar Estoque")
with col2:
    negative_button = st.button("Negativos")

if positive_button:
    st.session_state["show_mode"] = "positivo"
elif negative_button:
    st.session_state["show_mode"] = "negativo"
else:
    st.session_state["show_mode"] = "nenhum"

if st.session_state["show_mode"] == "positivo":
    result = df[positive]
elif st.session_state["show_mode"] == "negativo":
    result = df[negaitve]

if result is None:
    st.write("Escolha algum filtro")
else:
    st.write(result)
