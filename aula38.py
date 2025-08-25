#exercicio54 
#em python escreva uma função que recebe uma lista de números e calcula a média deles

def calcular_media(numeros):
    if not numeros:  # verifica se a lista está vazia
        return 0  
    return sum(numeros) / len(numeros)


# Exemplo de uso:
lista = [10, 20, 30, 40, 50]
media = calcular_media(lista)
print("A média é:", media)
