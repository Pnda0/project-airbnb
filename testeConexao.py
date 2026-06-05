from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1317@localhost:5432/airbnb_analysis"
)

with engine.connect() as conn:
    print("Conectado com sucesso!")


import pandas as pd

listings = pd.read_csv("data/processed/listings_clean.csv")
reviews = pd.read_csv("data/raw/reviews.csv")


# Enviar tabela
listings.to_sql(
    "listings", # Nome da tabela no postgres
    engine,
    if_exists="replace", # "replace" substitui a tabela se já existir. 
    index=False # Não envia o index do pandas para o banco como coluna
)


print("Tabela 'listings' enviada com sucesso!")

reviews.to_sql(
    "reviews",
    engine,
    if_exists="replace",
    index=False
)

print("Tabela 'reviews' enviada com sucesso!")