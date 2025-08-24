#exercicio 50
#crie uma função que faça a multiplicação de dois números
#este números devem ser passados por parâmetro

def multiplicar(num1, num2):
    return num1 * num2

# Programa principal
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado = multiplicar(n1, n2)

print(f"A multiplicação de {n1} x {n2} é: {resultado}")
