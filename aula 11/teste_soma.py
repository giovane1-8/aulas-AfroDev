def soma_dois_numeros(n1: int, n2: int) -> int:
    return n1 + n2

def divide_dois_numeros(n1,n2):
    if n2 == 0:
        return("não pode divir por zero")
    return n1/n2

def test_retorno_soma_dois_numeros():
    assert 3 == soma_dois_numeros(1,2)
    
def teste_divisao_com_numeros_validos():
    assert 2 == divide_dois_numeros(4,2)

def teste_divisao_por_zero():
    assert "não pode divir por zero" == divide_dois_numeros(1,0)

def teste_divisao_com_zero_a_esquerda():
    resultado = divide_dois_numeros(0,1)
    assert 0 == resultado
    
    
def teste_divisão_com_letras():
    assert 4 == divide_dois_numeros("4","2")