import streamlit as st
import pandas as pd
import plotly.express as px

# Remove as margens.
st.set_page_config(layout='wide')

# Tabelas - Cria duas tabelas a partir de valores importados em csv.
df_reviews = pd.read_csv("F:/Projects/Python/Asimov/projetos/top100_books/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("F:/Projects/Python/Asimov/projetos/top100_books/datasets/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max() # procura e retorna o maior valor da lista.
price_min = df_top100_books["book price"].min() # procura e retorna o menor valor da lista.

# Slider de Preços - Cria um slider capaz de ir do preço mínimo dos livros até o preço máximo.
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# Define que a seção de preços de livros será a seção afetada pelo slider de preços.
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
# Exibe o dataset.
df_books

# Gráficos - Cria os gráficos em barras e em forma de histograma com pandas.
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

# Divide os gráfics em duas colunas na tela, ao invés de um ficar embaixo do outro.
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)