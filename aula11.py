#Crie um algoritmo que receba as notas de um aluno e verifique se o aluno atingiu a média escolar que é seis
#Se o aluno atingiu a média mostrar aprovado senão mostrar reprovado

nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))
nota4 = float(input("Digite a quarta nota"))

media = (nota1 + nota2 + nota3 + nota4)/4

if(media >= 6):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")