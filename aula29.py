#Exercicio 26 
#crie um programa que receba a caregoria em valor numérico de um produto
#se for exiba que é uma bolsa
#se for dois exiba que é um tênis
#se for três exiba que é uma mochiça
#senão exiba a mensagem produto inválido

codigo = int(input("Digite o código do produto"))

if codigo ==1:
    print("Este produto é uma bolsa")
elif codigo == 2:
    print("Este produto é um tênis")
elif codigo == 3:
    print("Este produto é uma mochila")
else:
    print("Você digitou um código inválido")