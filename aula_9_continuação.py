# I/O
import os
os.system("cls")
import pandas as pd

df = pd.read_excel("estudo_io_aula_9.xlsx")
print(df.index)
print(df)
# df1 = df.dropna() remove a linha que tiver algum valor nulo em qualquer coluna
df1 = df.fillna(0) # insere um valor para os campos nulos



print(f"================= \n {df1}")


#print("================\n",df["nome"]) mostra somente a coluna nome

#print("================\n",df.loc[3])  acesso por linha
#print("================\n",df.loc[3, "saldo bancario"])  acesso por linha e coluna


print("================\n",df.sort_values(by="nome")) # ordena por coluna nesse caso por nome


df["teste"] = "teste" # cria nova coluna
del df["teste"] # deleta uma coluna

print(df.loc[[0,3], ["nome","saldo bancario"]]) # retorna multiplas linhas e expecifica 



