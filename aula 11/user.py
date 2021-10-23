class Usuario:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def boas_vindas(self):
        print(f"Bem vindo: {self.nome}, idade: {self.idade}")