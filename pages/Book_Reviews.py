import streamlit as st
import pandas as pd

# Remove as margens:
st.set_page_config(layout='wide')

# Importa as planilhas de dados em csv:
df_reviews = pd.read_csv("F:/Projects/Python/Asimov/projetos/top100_books/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("F:/Projects/Python/Asimov/projetos/top100_books/datasets/Top-100 Trending Books.csv")

# Expõe os nomes dos livros sem repetições:
books = df_top100_books["book title"].unique()

# Define uma caixa de seleção na barra lateral esquerda:
book = st.sidebar.selectbox("Books", books)

# Cria dois filtros -- Um filtro para o nome dos livros e um filtro para as avaliações com base no nome:
# Os filtros estarão ativos sempre que um livro esteja selecionado na caixa de seleção da barra lateral esquerda.
df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

# Isola o valor das strings por meio da função iloc[0], da mesma forma que o slicing em listas funciona:
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}" # Adiciona o simbolo '$' à string de preço.
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Define o Header da Página:
st.title(book_title)

# Define o SubHeader da Página:
st.subheader(book_genre)

# Define as 3 colunas de informação sobre os livros (preço, avaliação, ano de publicação):
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

# Cria uma linha divisora na página:
st.divider()

# Define e exibe o preço, genero e data de publicação dos livros.
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])