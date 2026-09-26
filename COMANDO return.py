def somar(a, b):
    resultado = a + b
    return resultado

valor = somar(10, 5)
print(valor)

def verificar_estoque(quantidade):
    if quantidade > 0:
        return "Disponivel"
    return "Indisponivel"

situação = verificar_estoque(5)
print( "situacao" )