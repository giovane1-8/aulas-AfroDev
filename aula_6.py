# importar modulo 
import random
escolha_jogador =''
numero_jogador = 0
numero_robo = 0
resulta_impar_par = 0
resultado_soma = 0
pontos_jogador = 0
pontos_robo = 0
print("VAMOS JOGAR IMPAR OU PAR !!!!")
while True:
    print("###### INICIO DE RODADA ######")
    print("Você escolhe impar ou par ? (i) impar (p)par")
    escolha_jogador = input().upper()
    while True: 
        if(escolha_jogador == "I"):
            print('O jogador escolheu impar nessa rodada\n')
            break
        elif escolha_jogador == "P":
            print('O jogador escolheu par nessa rodada\n')
            break
        else:    
            print("escolha somente i ou p: ")
            escolha_jogador = input().upper()
            
    print("ESCOLHA UM NUMERO DE 0 A 10: ")
    while True:
        try:
            numero_jogador = int(input())
            while True:
                if 0 <= numero_jogador <= 10:
                    break
                else:
                    print("Coloque somente numeros de 0 a 10: ")
                    numero_jogador = int(input())
            break
        except ValueError:
            print("coloque somente numeros reais: ")
    numero_robo = 1
    print(f"\nRobo: Eu escolho {numero_robo}\n")

    resultado_soma = numero_robo + numero_jogador
    resulta_impar_par =  resultado_soma % 2 == 0
    print("O RESULTADO DEU:", resultado_soma)
    
    if escolha_jogador == "P" and resulta_impar_par:
        pontos_jogador += 1
        print("O usuario venceu !")
    elif escolha_jogador == "I" and not resulta_impar_par:
        pontos_jogador += 1
        print("O usuario venceu !")
    else:
        pontos_robo += 1
        print("O robo venceu !")
    
    print(f"\nPONTOS JOGADOR: {pontos_jogador} \nPONTOS ROBO: {pontos_robo}\n")
    if pontos_jogador >= 2:
        print("O JOGADOR VENCEU !!!")
        break
    elif pontos_robo >= 2:
        print("O ROBO VENCEU !!!")
        break
        
            
            
