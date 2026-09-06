maior_numero = float('-inf')  # Inicializa com o menor número possível

print("Por favor, digite 5 números:")
for i in range(5):
    while True:
        try:
            numero_digitado = int(input(f"Digite o {i+1}º número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if numero_digitado > maior_numero:
        maior_numero = numero_digitado

print(f"O maior número digitado foi: {maior_numero}")
