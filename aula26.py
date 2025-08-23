#exercício 23
#crie um programa que receba um valor de salário e se ele for menor ou igual a 1800 mostra a mensagem você não precisa declarar imposto de renda senão mostre a mensagem você precisa declarar imposto de renda

salario = float(input("Qual o seu salário"))

if salario <= 1800:
    print("Você não é precisa declarar imposto de renda")
else:
    print("Você precisa declarar imposto de renda")