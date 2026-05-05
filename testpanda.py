import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

st.title("Deputados 2022")

uf = st.text_input("Digite a sigla dos deputados:")

if uf:
filtrado = df[df['uf'] == uf.upper()]
st.dataframe(filtrado[['nome', 'uf', 'partido']])


