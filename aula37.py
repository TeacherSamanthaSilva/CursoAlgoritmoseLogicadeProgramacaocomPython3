#exercicio 37 
#escreva uma função que receba uma lista de números e retorne apenas os números pares da lista

def filtrar_pares(lista):
    """Retorna apenas os números pares de uma lista."""
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(numeros)
print(resultado)  # Saída: [2, 4, 6, 8, 10]
