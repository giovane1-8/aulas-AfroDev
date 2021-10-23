from user import Usuario
usuario1 = Usuario(nome="Giovane",idade=18)
usuario1.boas_vindas()

usuario1.nome = "Giovane teste"
delattr(usuario1, "idade") # deleta um atributo
print(usuario1.nome)

