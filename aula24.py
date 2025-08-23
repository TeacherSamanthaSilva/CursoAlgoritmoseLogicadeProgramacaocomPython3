#exercicio 21
#crie um algoritmo que leia o número de rodas de um veículo se for menor ou  igual a 2 mostra a mensagem você não precisa pagar pedágio se for maior que duas mostrar a mensagem você precisa pagar pedágio

rodas = int(input("Quantas rodas tem seu veículo? "))

if(rodas <= 2):
    print("Você não precisa pagar pedágio")
else:
    print("Você precisa pagar pedágio")
