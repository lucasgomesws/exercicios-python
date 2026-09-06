# programa para dizer se o estudante foi aprovado ou nao
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3
print("a sua media é:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
