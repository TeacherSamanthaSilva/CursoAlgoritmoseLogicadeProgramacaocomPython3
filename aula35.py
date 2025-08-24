#exercicio51
#crie uma função que retorna se um número é maior ou menor que 10
#número deve ser passado por parâmetro

def verifica_numero(numero):
    if numero > 10:
        return "Maior que 10"
    elif numero < 10:
        return "Menor que 10"
    else:
        return "Igual a 10"

# Programa principal
num = int(input("Digite um número: "))
print(verifica_numero(num))
