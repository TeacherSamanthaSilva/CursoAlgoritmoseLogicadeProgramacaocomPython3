#Crie um algoritmo que receba uma saudação e um nome de uma pessoa e mostre essas informações na tela

saudacao = str(input("Digite uma saudação "))
nome = str(input("Digite seu nome"))

textocompleto = (saudacao + " Sr(a) " + nome)
print(textocompleto)