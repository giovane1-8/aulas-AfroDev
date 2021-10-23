import os
os.system("cls")
# funções

def deseja_boa_tarde():
    print("Boa tarde")

def exibe_a_palavra_enviada(palavra):
    print(f"A palavra enviada foi {palavra}")

def remove_espaços_antes_e_depois(palavra):
    return palavra.strip()

var = "       oi    "
print(var)
var = remove_espaços_antes_e_depois(var)
print(var)

def convida_pessoas(nome):
    return nome

nome = convida_pessoas("Giovane")
print(nome)

def nome_na_lista(*args):
    print(type(args))
    
os.system("cls")
quem_vai = {}
"""
quem_vai = input("Digite seu nome, se for à festa: ")
com_acompanhante = input("Digite o nome do acompanhante: ")
a = input()
b = input()
c = input()
nome_na_lista(quem_vai,com_acompanhante,a,b,c)
"""
os.system("cls")

def soma(*args):
    print(sum(args))
    
#soma(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))

def formulario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

formulario(nome="Giovane", sobrenome="lima",idade=23)

# ZeroDivisionError
# NameError (não encontra valiavel)
# typeError (Erro tipo de dados)
# ConnectionError 
# ValueError

"""COMO FORÇAR UM ERRO NO CODIGO"""

os.system("cls")
def teste_erro():
    raise ValueError

teste_erro()