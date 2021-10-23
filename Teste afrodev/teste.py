# Apresente: quantidade de linhas e colunas no arquivo, idade máxima, idade mínimae idade média.
# Liste todos os registros da atleta Serena Williams.
# Liste o nome de todos os países distintos que participaram das olimpíadas.
# Liste os atletas que receberam mais de 3 medalhas de ouro.
# Liste todos os atletas do esporte natação e do país Brasil.

import pandas as pd

import os

def enter_continua():
    input()
    os.system("clear")

df = pd.read_csv("base.csv") # cria o dada frame
print(df[df["idade"] == 15])

print(df)

print("Anos com mais medalhas:")
grupo_medalha_por_ano = df.groupby('ano')
medalha_ano = grupo_medalha_por_ano[['total']].sum() # Medalhas por ano
print(medalha_ano.sort_values('total', ascending = False)) 
enter_continua()


print("Paises com mais medalhas:") 
paises_medalha = df.groupby('pais')
dados_melhores_paises = paises_medalha[['total','pais']].sum() # paises com mais medalhas
print(dados_melhores_paises.sort_values('total', ascending = False).head(6)) 
enter_continua()

print("Atletas que tem mais medalhas:")
grupo_atleta = df.groupby('atleta')
dados_melhores_atletas = grupo_atleta[['total','atleta']].sum()# atletas com mais medalhas
print(dados_melhores_atletas.sort_values('total', ascending = False).head(6))
enter_continua()

print("Atletas do Brasil na Natanção")
print(df.loc[(df["esporte"] == "Swimming") & (df["pais"] == "Brazil")].reset_index(drop = True)) #
enter_continua()

print("Pessoas que receberam mais que 3 medalhas de ouro")
print(df.loc[df["ouro"] > 3]) # Pessoas que receberam mais que 3 medalhas de ouro
enter_continua()

print("Paises que participaram nas olimpiadas:")
print(df["pais"].drop_duplicates().reset_index(drop = True)) # paises que participaram nas olimpiadas 
enter_continua()

print("Mostras todas as linhas da Serena Williams")
print(df.loc[ df["atleta"] == "Serena Williams" ]) # Mostras todas as linhas da Serena Williams
enter_continua()

print("Media de idade das olimpiadas:")
print(df["idade"].mean()) # Media de idade das olimpiadas
enter_continua()

print("Pessoa com idade minima na Olimpiada:")
print(df["idade"].min()) # Mostra idade minima
enter_continua()

print("Pessoa com idade maxima na Olimpiada:")
print(df["idade"].max()) # Mostra idade maxima
enter_continua()

print("Quantidade de colunas:")
print(len(df.loc[0])) #quantidade de colunas
enter_continua()

print("Quantidade de linhas:")
print(len(df)) #quantidade de linahs
enter_continua()
