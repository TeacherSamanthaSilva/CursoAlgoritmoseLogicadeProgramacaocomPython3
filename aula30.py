#Exercício 27
#crie um programa que leia a renda de um usuário e de acordo com a renda mencionada mostre qual será o limite esse cliente receberá. 

renda = float(input("Digite a sua renda "))

if renda < 2000:
    print("Sua renda é abaixo do mínimo para possuir este cartão de crédito")
if renda >= 2000:
    print("Você receberá um limite de 1000 reais")
if renda >= 4000: 
    print("Você receberá um limite de 2000 reais")
if renda >= 6000 and renda <= 10000:
    print("Você receberá um limite te de 3000 reais")
if renda >=10000:
    print("Você tem um perfil para cartões Black fale com nosso gerente")