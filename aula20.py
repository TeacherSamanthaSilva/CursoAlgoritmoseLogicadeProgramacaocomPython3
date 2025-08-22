#Exercicio 16
#crie um algoritmo que receba o valor do salario e o valor do aumento e mostra a soma dos dois

salario = float(input("Digite o valor do salário"))
aumento = float(input("Digite o valor do aumento"))
novosalario = salario + aumento 
print(f"O salário deste funcionário que antes era R${salario} recebeu um aumento de R${aumento} e agora é R${novosalario}")