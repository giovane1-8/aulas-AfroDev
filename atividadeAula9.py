#Criar uma nova coluna com a idade das pessoas.
#Exibir que tem o maior e o menor salário.
#Exibir quem tem o maior e o menor saldo bancário.
#Exibir quem tem o maior e o gasto acumulado.
#Exibir a média de gastos de cada um. (editado) 
import pandas as pd

#variaveis controladoras 

maior_salario = 0
menor_salario = 0
maior_gasto_acumulado = 0
menor_gasto_acumulado = 0
maior_gasto_acumulado_nome = ""
menor_gasto_acumulado_nome = ""
nome_maior_salario = ""
nome_menor_salario = ""

df = pd.read_excel("estudo_io_aula_9.xlsx")
df["Idade"] = (2021 - df["ano nascimento"])
df = df.fillna(0)

for key, valor in df["saldo bancario"].items():
    if valor > maior_salario:
        maior_salario = valor
        nome_maior_salario =  df["nome"][key]

menor_salario = maior_salario

for key, valor in df["saldo bancario"].items():
    if valor < menor_salario:
        menor_salario = valor
        nome_menor_salario = df["nome"][key]

for key, valor in df["gastos co estudos"].items():
    soma = valor + df["gastos com alimentação"][key] + df["gastos com moradia"][key]
    if soma > maior_gasto_acumulado:
        maior_gasto_acumulado = soma
        maior_gasto_acumulado_nome = df["nome"][key]

menor_gasto_acumulado = maior_gasto_acumulado
for key, valor in df["gastos co estudos"].items():
    soma = valor + df["gastos com alimentação"][key] + df["gastos com moradia"][key]
    if soma < menor_gasto_acumulado:
        menor_gasto_acumulado = soma
        menor_gasto_acumulado_nome = df["nome"][key]
        

df["media de gastos"] = (df["gastos co estudos"] + df["gastos com alimentação"] + df["gastos com moradia"]) / 3 

#printa a idade e nome de todos
print("\n\n",df.loc[list(range(len(df))),["nome", "Idade"]])

#printa menor e maior salario
print(f"######## Maior salario é da: {nome_maior_salario} com: {maior_salario} ########\n######## Menor salario é da {nome_menor_salario} com: {menor_salario} ########")

#printa o maior e menor gasto acumulado
print(f"\n\nmaior gasto acumulado é da {maior_gasto_acumulado_nome} com: {maior_gasto_acumulado}\nO menor gasto acumulado é da {menor_gasto_acumulado_nome} com {menor_gasto_acumulado}")

# printa a media de dastos de todos
print("\n\n",df.loc[list(range(len(df))),["nome", "media de gastos"]])
