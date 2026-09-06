peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura (m ou cm): "))

# Ajuste automático de altura (cm para m)
if altura > 3:
    altura /= 100

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"\n--- Resultado ---")
print(f"Peso: {peso} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {categoria}")
