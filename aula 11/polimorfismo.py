class Carros():
    idade = None
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    def set_idade(self, idade):
        self.idade = idade
        
class Astra(Carros):
    def __init__(self, nome, cor,ano):
        self.ano = ano
        super().__init__(nome, cor)
    def get_idade(self):    
        print(self.idade)

a = Astra(nome="Spin",cor="cinza",ano=2012)
a.set_idade(18)
a.get_idade()