#dicionarios 
dicionario = {"nome": "Giovane de Lima", 
              "idade": 32, 
              "formacao": {"etec": "Tec. Inf. p/ internet", "federal cubatao": "lic. matematica"},
              "teste": "teste"
              }
print(dicionario)
print(len(dicionario))

"""
EM JSON USAR VALOR NULO
COMO:

ex = {"valor": Null}
"""
print(dicionario.get("nome","não existe")) # manipulando o valor retornado caso não exista
print(dicionario.keys()) #mostras as chaves 
print(dicionario.values()) #mostras os valores 
print(dicionario.items()) # acessando valores e chaves do dicionario
del dicionario["teste"]


dic = dicionario.get("formacao","não existe")
print("######",dic.get('etec'),"########") #dicionario dentro de outro dicionario

dicionario['idade'] = 18 # Mudando valor de uma chave
print(dicionario["idade"])
for key, value in dicionario.items():
    print(f"valor= {value} \nkey = {key} \n --------")
    
var = dict(nome = "aaaa")

#CONJUNTOS
conjunto1 = {1,2,3}
conjunto2 = {3,4,5,6}

print(conjunto1.union(conjunto2)) # Une os conjuntos 

print(conjunto1.intersection(conjunto2)) # intersecção dos dois conjuntos

# conjunto1.update(conjunto2) faz a união do conjunto2 no conjunto1 
print(conjunto1 < conjunto2)

print(conjunto2 - conjunto1)
#FUNCÇÃO

# teste_teste = variavel
# teste_teste() = função 
# TesteTeste() = Classe 

def print_uma_palavra():
    print("uma palavra ")









