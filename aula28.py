#Exercicio25
#escreva um programa que leia um número
#se o número for maior ou igual a 10 mostre uma mensagem dizendo que número precisa ser maior ou igual a dez
#se número for menor que 20 multiplique por 2
#senão multiplique por 5

numero = int(input("Digite um número qualquer "))

while numero < 10:
    print("Você precisa digitar um número maior que 10")
    numero = int(input("Digite um número qualquer "))
if numero <= 20:
    produto = numero * 2
    print(f"O valor de {numero } multiplicado por 2 é: {produto}" )
else:
    produto = numero * 5
    print(f"O valor de {numero } multiplicado por 2 é: {produto}" )