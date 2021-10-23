""" Para que serve a função range()"""
range(10) #intervalo do 0 ao 9 
range(-100, 100) # intervalo de -100 ao 99
range (-100, 100, 10) # intervalo de -100 ao 99 de 10 em 10 

print(range(10)) # vai mostrar somente o numero inicial e o final da sequencia


var = range(10)
var = list(var)
print(var) # vai mostrar a sequencia de 0 a 9

#ou 

var = list(range(10)) 
print(var)

#ou

print(list(range(10))) 
""" 


+ soma
- subtração
* multiplicação
/ divisão 
**



"""
num = 1
num += 1 # soma com o valor que a variavel ja tem 
print(num) 


"""
    operadores de membro 
    in = se tal numero ou str esta dentro de uma lista
    not in = se tal numero ou str NÃO esta dentro de uma lista
"""
var_op_membro = list(range(0,1000,100))
print(var_op_membro) 
print (100 in var_op_membro)
print (-1 not in var_op_membro)

#IF
#ELIF
#ELSE 

num_if = 7
if num_if == 7:
    print("estou no if")
elif num_if == 7:
    print("Estou no elif")
else:
    print("estou no else")
    
    
print('Qual é a sua idade ?')
idade = int(input())

idade_acompanhante = None
if idade >= 18:
  print("Você pode entrar")
elif idade == 17:
  print("voce esta acompanhado ?")
  esta_acompanhado = input()
  if esta_acompanhado != "sim" :
    print("você não pode entrar sem acompanhante")
  else:
    print("Quantos anos tem seu acompanhante ?")
    idade_acompanhante = int(input())
    if idade_acompanhante > 17:
      print("você pode entrar com acompanhante")
    else:
      print("você e seu acompanhante não tem idade suficiente")
else:
  print("você não pode entrar")