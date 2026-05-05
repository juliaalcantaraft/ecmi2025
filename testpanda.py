import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

sigla = st.text_input('Digite a Sigla do Partido')
uf = st.text_input('Digite a UF')

if sigla:
   df_filtrado = df[df['partido'] == sigla.upper()]
else:
    df_filtrado = df

if uf:
   df_filtrado = df_filtrado[df_filtrado['uf'] == uf.upper()]

st.dataframe(df_filtrado)

# Gráfico
st.subheader('Deputados por Partido')
grafico = df_filtrado['partido'].value_counts()
st.bar_chart(grafico)

