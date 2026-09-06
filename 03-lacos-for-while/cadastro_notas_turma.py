# Sistema de Cadastro de Notas

total_alunos = int(input("Quantos alunos? "))
aprovados = 0
reprovados = 0

for _ in range(total_alunos):
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))

    if nota >= 7:
        print("Aprovado")
        aprovados += 1
    else:
        print("Reprovado")
        reprovados += 1

print(f"\nTotal de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")
