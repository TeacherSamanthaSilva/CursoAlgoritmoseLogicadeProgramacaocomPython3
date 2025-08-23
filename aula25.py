#exercício22
#cria um algoritmo que lê dois número e diz qual dos dois é o maior

primeironumero = int(input("Digite o primeiro numero"))
segundonumero = int(input("Digite o segundo numero"))

if(primeironumero > segundonumero):
    print("O primeironumero é maior que o segundonumero")
elif (segundonumero > primeironumero):
    print("O segundonumero é maior que o primeironumero")
else:
    print("Ambos os números são iguais")