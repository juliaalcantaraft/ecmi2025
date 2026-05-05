import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

st.title("Deputados 2022")
st.dataframe(df[['nome', 'uf', 'partido']])


