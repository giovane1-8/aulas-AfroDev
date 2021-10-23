#aula sobre arrays
#estudar metodos de array 
lista1 = [1,2,3]
lista2 = ["a","b","c"]

lista1.extend(lista2)
print(lista1)


lista_vazia = []
lista_com_dados = [1, 2, "Cassio"]
lista_segunda_forma = list()
lista_com_dados.append("Rodrigues")
# lista_com_dados.clear()
lista_com_dados.extend([1, 2, 3, "Azul", "Verde"])
# print(lista_com_dados.index(2, 1, 4))
'''if "teste" in lista_com_dados:
  print(lista_com_dados.index("teste")) # retorna um numero com a posição do indice
  sobrenome = lista_com_dados[lista_com_dados.index("Rodrigues")] 
  print(sobrenome)'''

# lista_com_dados.insert(1, "teste -1")
# del lista_com_dados[0]
# lista_com_dados.pop(8)
# lista_com_dados.remove("Azul")
lista_com_dados[8] = "Rosa"
# print(str(lista_com_dados[7]).replace("+", ""))
lst = [1, 2, 3, 6, 4, 5]
print(lst)
lst.sort(reverse=True)
print(lst)

print(lista_com_dados)
lista_com_dados.reverse()
print(lista_com_dados)
print(len(lista_com_dados))

dir(lista_com_dados)
"""
'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
 """

help(lista_com_dados.sort)

help(len)

# list comprehention
#[expressão "condicional/iterador" cada elemento da lista]

lista = list(range(10))
lista1 = []
print(lista)
for numero in lista:
  if numero < 5:
    lista1.append(numero)

print(lista1)

lista_nova = list(range(10))
print(lista_nova)
lista2 = [x for x in lista_nova]
print(lista2)
lista3 = [nome if nome<5 else nome*2 for nome in lista_nova]

lista_1 = range(0, 11, 2)
teste = 5
result = [numero*teste for numero in lista_1]

i = 0
n = 55
j = 5
teste1 = list(range(i, n , j))
print(teste1)