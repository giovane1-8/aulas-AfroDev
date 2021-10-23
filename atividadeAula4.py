# Imagina que estamos fazendo um sistema para uma escola
# E esse vai definir se o aluno foi aprovado ou não
# condições aprovação media de 4 notas >= 7
# numero de faltas, tem que ser menor que 4
# o sistema vai receber o nome, as notas e as faltas e vai exibir o nome e o status 
# Aprovado ou reprovado.
# não sei a quantidade de notas
# não sei a média
# não sei a quantidade de faltas permitidas
# Print as mensagem de acordo com a identidade escolhida.


""" VARIAVEIS DE CONTROLE """
nota_aluno = 0
faltas_aluno = 0
media_aluno = 0
nome_aluno = ""
semestres = []
media_aprovacao = 5
media_recuperacao = 4
faltas_para_reprovacao = 0
"""FUNÇÕES"""
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
    except ValueError: #Acontece se não for possivel transformar a variavel nota em float
        print(f"NOTA INVALIDA \n Digite novamente a no do {semestre}º semestre : ")
        validar_nota(input())
                
""" CONFIGURAÇÃO DO SISTEMA """
print("########## CONFIGURAÇÃO DO SISTEMA ##########")
print("Digite a quantidade de semestres: ")                
while True:
    try: #inicio de verificação por erro
        semestres = list(range(1,int(input())+1))
        break
    except ValueError: # se o usuario digitar letras ou só espaços
        print("NUMERO INVALIDAS \n Digite somente numeros inteiros \n Digite a quantidade de semestres: ")

print("Digite a media de aprovação: ")
while True:
    try: #inicio de verificação por erro
        media_aprovacao = float(input())
        break
    except ValueError: # se o usuario digitar letras ou só espaços
        print("NUMERO INVALIDAS \n Digite somente numeros inteiros: \n Digite a media de aprovação:")

print("Digite a media de recuperação: ")
while True:
    try: #inicio de verificação por erro
        media_recuperacao = float(input())
        while media_recuperacao > media_aprovacao:
            print("A media de recuperação não pode ser maior que a media de aprovação \n digite novamente: ")
            media_recuperacao = float(input())
        break
    except ValueError: # se o usuario digitar letras ou só espaços
        print("NUMERO INVALIDAS \n Digite somente numeros inteiros \n  Digite a media de recuperação:")

print("Digite a quantidade de faltas para reprovação: ")
while True:
    try: #inicio de verificação por erro
        faltas_para_reprovacao = int(input())
        break
    except ValueError: # se o usuario digitar letras ou só espaços
        print("NUMERO INVALIDAS \n Digite somente numeros inteiros \n Digite a quantidade de faltas para reprovação: ")

print("########## INICIO CADASTRO DE NOTAS DE ALUNO ##########")
""" INICIO DO FORMULARIO """
print("Qual o nome do  aluno ?")
nome_aluno = input()
while True:
    if nome_aluno.isalpha():
        break
    else:
        print("NOME INVALIDO \n Digite o nome composto só por letras:")
        nome_aluno = input()
for semestre in semestres:
    print(f"Digite a nota do {semestre}º semestre")                         
    validar_nota(input()) #inicia a nossa função de verificação de input    
    
print("Digite quantas faltas o aluno tem: ")
while True:
    try: #inicio de verificação por erro
        faltas_aluno = int(input())
        break
    except ValueError: # se o usuario digitar letras ou só espaços
        print("FALTAS INVALIDAS \n Digite somente numeros inteiros: ")
        


""" CONFIGURAÇÃO DE MENSAGENS AO USUARIO """
mensagem_inicio = f"O aluno {nome_aluno} esta"
mensagem_aprovado = "aprovado"
mensagem_recuperacao = "de recuperação"
mensagem_reporvado_nota = "reprovado por nota"
mensagem_reprovado_nota_falta = "reprovado por falta e nota"
mensagem_provado_falta = "reprovado por falta"


""" COMEÇA O TRATAMENTO E VERIFICAÇÃO DE DADOS """
media_aluno = nota_aluno / len(semestres) #pagamos a media das notas fornecidas 
print(mensagem_inicio, end=" ")
if faltas_aluno < 4: # verifica se o aluno teve a quantidade de aulas minimas 
    if media_aluno >= media_aprovacao: #verifica se o aluno teve media suficiente para passar
        print(mensagem_aprovado)
    elif media_aluno > media_recuperacao: # varifica se o aluno teve nota para recuperação 
        print(mensagem_recuperacao)
    else: # se o aluno não foi aprovado nem esta de recuperação
        print(mensagem_reporvado_nota)
elif faltas_aluno > faltas_para_reprovacao and media_aluno < media_recuperacao: # se o aluno não assistiu a quantidade minimas de faltas
    print(mensagem_reprovado_nota_falta)
else:
    print(mensagem_provado_falta)
print(f"Media do aluno: {media_aluno}")
print(f"Faltas: {faltas_aluno}")