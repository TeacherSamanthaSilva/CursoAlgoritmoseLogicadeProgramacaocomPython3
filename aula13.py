#Crie um algoritmo que leia um valor de velocidade e diga se a pessoa ultrapassou ou não o limite de velocidade

velocidade = int(input("Digite o valor da velocidade"))

if(velocidade > 80):
    print("Você ultrapassou o limite de velocidade")
else:
    print("Você passou na velocidade permitida")