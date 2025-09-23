import streamlit as st
import pandas as pd
from defs import treatments

uploaded_file =  st.file_uploader("Envie seu CSV", type="csv")

st.title("ANÁLISE SEMANAL")
if uploaded_file is not None:
    raw_data = pd.read_csv(uploaded_file, sep=";")
    tbl_stock_summary = treatments(raw_data)
<<<<<<< HEAD
    st.write(tbl_stock_summary)
=======
    st.write(tbl_stock_summary)
    
>>>>>>> 7109851 (debug: add temporary logs to check Entrada and Saida columns)
