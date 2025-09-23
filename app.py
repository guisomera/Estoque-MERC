import streamlit as st
import pandas as pd
from defs import treatments

uploaded_file =  st.file_uploader("Envie seu CSV", type="csv", accept_multiple_files=True)

st.title("ANÁLISE DE ESTOQUE")
if uploaded_file is not None:
    raw_data = pd.read_csv(uploaded_file, sep=None, engine="python")
    tbl_stock_summary = treatments(raw_data)
    st.write(tbl_stock_summary)
    