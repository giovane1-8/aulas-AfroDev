# orientação a objeto 

#cria uma caixa
class Carro:
    carro1 = "Astra 99 foguete"
    carro2 = "Gol quadrado motor ap"
    carro = "uno com escada no teto"
    
class Pessoa:
    
    def acao_fala(self):
        print("Boa noite")

#INSTANCIANDO CLASSE
pessoa1 = Pessoa()
#criando atributos
pessoa1.nome = "Giovane"
pessoa1.idade = 32

#executa um metodo
pessoa1.acao_fala()

#print(Carro.carro1)

print(pessoa1.nome, pessoa1.idade)


