#stdlib
import streamlit as st

#third-party
import pandas as pd
import io
import plotly.express as px

#Local
from defs import treatments, concat_treaments, get_balance

st.set_page_config(page_title="Análise de Estoque", layout="wide", initial_sidebar_state="expanded")        #Criaçaõ de sidebar e configuração da pagina  
st.title("ANÁLISE DE ESTOQUE")      #Titulo do site 

col1, = st.columns(1)                       #Sepração de colunas pra poder trabalhar em diferentes partes do site 
col2, col3 = st.columns (2, gap="large")



with st.sidebar:                #"NA SIDEBAR"
    st.subheader("Envie seu documeto")          
    uploaded_file =  st.file_uploader("XLSX até 200MB", 
                                      type="xlsx", 
                                      accept_multiple_files=True)    #Uploa de arquivos 


if not uploaded_file:
    st.info("Faça o upload do arquivo para ver a análise")
elif uploaded_file:
    summaries = []
    for doc in uploaded_file:
        try:        #Pega os valores em bytes
            buf= io.BytesIO(doc.getvalue())           #Faz um arquivo fake 
            df_raw = pd.read_excel(buf, engine="openpyxl")      #Le o arquivo
        
            summary_df = treatments(df_raw)             #Trata os dados
            summaries.append(summary_df)    
        except Exception as e:
            st.error(f"Falha ao processar {doc.name}: {e}")        

    concated_df = pd.concat(summaries)
    st.session_state["final_df"] = concat_treaments(concated_df)

    with col1:
        st.write(concated_df)
    
    balance = get_balance(concated_df)
    fig = px.pie(balance, values="Valor", names="Categoria", color='Categoria', 
             color_discrete_map={"Entrada": "#27AE60",
                                 "Saida": "#C0392B",
                                 "Estoque": "#7F8C8D"})
    col2.plotly_chart(fig)
