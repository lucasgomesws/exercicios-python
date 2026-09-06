numero = int(input("Digite um número (diferente de zero para continuar): "))

while numero == 0:
    print("Número inválido! Por favor, digite um número diferente de zero.")
    numero = int(input("Digite um número (diferente de zero para continuar): "))

print(f"Você digitou: {numero}. O programa continua.")
