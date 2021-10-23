# Imagina que estamos fazendo um sistema para uma escola
# E esse vai definir se o aluno foi aprovado ou não
# condições aprovação media de 4 notas >= 7
# numero de faltas, tem que ser menor que 4
# o sistema vai receber o nome, as notas e as faltas e vai exibir o nome e o status 
# Aprovado ou reprovado.

#Variaveis de controle
nota_aluno = 0
faltas_aluno = 0
media_aluno = 0
nome_aluno = ""

def validar_nota(nota): #função de verificação de input
    try: #tratamento de exceção 
        while True: #cria um enquanto infinito 
            nota = float(nota) # se a conversão da string nota der ValueError
                               # esse codigo não sera execultado e passara para o except
                               # onde esta o codigo que devera ser execultado se der ValueError
            if 0 <= nota <= 10: #verifica se a nota do semestre é valida
                global nota_aluno  
                nota_aluno += nota
                break # sai do while o enquanto infinito 
            else: #pede a nota do semestre novamente e volta ao ciclo
                print("NOTAS VALIDAS DE 0 A 10: \n Digite novamente: ")
                nota = input()
    except ValueError:          #Acontece se não for possivel transformar a variavel nota em float
        print("NOTA COMPUTADA COMO 0 \n")
                
""" INICIO DO FORMULARIO """

print("Qual o nome do  aluno ?")
nome_aluno = input()
if not nome_aluno or not nome_aluno.strip(): # verifica se o nome é composto só de espaços ou é None
  nome_aluno = "sem nome"
print("Digite a nota do primeiro Trimestre: ")
validar_nota(input()) #inicia a nossa função de verificação de input
print("Digite a nota do segundo Trimestre: ")
validar_nota(input())
print("Digite a nota do terceiro Trimestre: ")
validar_nota(input())
print("Digite a nota do quarto Trimestre: ")
validar_nota(input())
print("Digite quantas faltas o aluno tem: ")
try: #inicio de verificação por erro
    faltas_aluno = int(input())
except: #parece para qualquer execção dada dentro do try
    print("Faltas computada como 0")
    
""" COMEÇA O TRATAMENTO E VERIFICAÇÃO DE DADOS """

media_aluno = nota_aluno / 4 #pagamos a media das notas fornecidas 
print(f"O aluno {nome_aluno} esta", end=" ")
if faltas_aluno < 4: # verifica se o aluno teve a quantidade de aulas minimas 
    if media_aluno >= 7: #verifica se o aluno teve media suficiente para passar
        print("aprovado")
    elif 7 > media_aluno > 6: # varifica se o aluno teve nota para recuperação 
        print("de recuperação")
    else: # se o aluno não foi aprovado nem esta de recuperação
        print("reprovado por nota")
elif faltas_aluno > 3 and media_aluno < 6: # se o aluno não assistiu a quantidade minimas de faltas
    print("reprovado por falta e nota")
else:
    print("reprovado por falta")
print(f"Media do aluno: {media_aluno}")
print(f"Faltas: {faltas_aluno}")
