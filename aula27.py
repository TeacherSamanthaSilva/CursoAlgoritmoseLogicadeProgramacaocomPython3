#exercicio24 
#crie um programa que leia dois número e faça a multiplicação entre eles e se o produto foi maior que 100 mostre a mensagem esse número é alto senão mostre a mensagem este número é baixo

primeironumero = int(input("Digite o primeiro número "))
segundonumero = int(input("Digite o segundo número "))

produto = primeironumero * segundonumero

if produto <= 100:
    print("Este número é baixo")
else:
    print("Este número é alto")