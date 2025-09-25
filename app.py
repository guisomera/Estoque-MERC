import streamlit as st
import pandas as pd
import io
from defs import treatments, concat_treaments

uploaded_file =  st.file_uploader("Envie seu CSV", type="csv", accept_multiple_files=True)

st.title("ANÁLISE DE ESTOQUE")
if uploaded_file:
    summaries = []
    for doc in uploaded_file:
        file_byte = doc.getvalue()
        csv_text = file_byte.decode()
        buffer= io.StringIO(csv_text)
        df_raw = pd.read_csv(buffer, sep=None, engine="python")
        summary_df = treatments(df_raw)
        summaries.append(summary_df)

    concated_df = pd.concat(summaries)
    final_df = concat_treaments(concated_df)
    st.write(final_df)
    