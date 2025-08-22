#exercicio 18
#crie um programa que receba o saldo de uma conta bancária
#depois faça um deposito e um saque e mostre de forma dinâmica o saldo atual

saldonaconta = 359.56

deposito = float(input("Digite quanto você quer depositar "))
saldoatual = saldonaconta + deposito
saque = float(input("Digite quanto você quer sacar"))
saldoatual = saldoatual - saque
print("O saldo atual desta conta %.2f " %saldoatual)