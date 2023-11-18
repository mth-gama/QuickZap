import streamlit as st
import sqlite3
import pandas as pd

# Configuração para exibir mais linhas e colunas no DataFrame
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)

# Conexão com o banco de dados
conn = sqlite3.connect('database.db')


def exibir_dados_tabela():
    query = "SELECT * FROM Mensagens"
    df = pd.read_sql(query, conn)
    st.dataframe(df.iloc[:, 1:])

exibir_dados_tabela()

conn.close()
