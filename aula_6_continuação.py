# importar modulo 
# importar modulo 
import random
escolha_robo_1 =0 
resulta_impar_par = 0
pontos_robo_1 = 0
pontos_robo_2 = 0
rodadas = 0
vitorias_robo_1 = 0
vitorias_robo_2 = 0
count = 1
print("VAMOS JOGAR IMPAR OU PAR !!!! \n Quantas rodadas você quer que os robos joguem ?")
while True:
    try:
        rodadas = list(range(1,int(input())+1))
        break
    except ValueError:
        print("Digite somente numeros inteiros: ")
if len(rodadas) % 2 == 0:
    print("######## Numero par, poderá ocorrer um empate ########")
print()
for rodada in rodadas:
    for n in range(3):
        escolha_robo_1 = random.randrange(2)
        resulta_impar_par = (random.randrange(11) + random.randrange(11)) % 2 == 0
        if escolha_robo_1 == 0 and resulta_impar_par:
            pontos_robo_1 += 1
        elif escolha_robo_1 == 1 and not resulta_impar_par:
            pontos_robo_1 += 1
        else:
            pontos_robo_2 += 1
    if pontos_robo_1 > pontos_robo_2: 
        vitorias_robo_1 += 1
    elif pontos_robo_2 > pontos_robo_1:
        vitorias_robo_2 += 1
    pontos_robo_1 = 0
    pontos_robo_2 = 0
if vitorias_robo_1 > vitorias_robo_2:
    print(F"\n######## ROBO 1 VENCEU {vitorias_robo_1} PARTIDAS ########")
    print(F"Vitorias do robo 2: {vitorias_robo_2}")
elif vitorias_robo_1 == vitorias_robo_2:
    print("######## OS ROBOS EMPATARAM ########")
    print(f"######## PONTOS ROBO 1: {vitorias_robo_1} ######## \n########  PONTOS ROBO 2: {vitorias_robo_2} ########")
else:
    print(F"\n######## ROBO 2 VENCEU {vitorias_robo_2} PARTIDAS ########")
    print(F"Vitorias do robo 1: {vitorias_robo_1}")
print(f"{len(rodadas)} rodadas")
   