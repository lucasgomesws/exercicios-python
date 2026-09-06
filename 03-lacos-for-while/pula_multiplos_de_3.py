print("numeros de 1 a 10, exceto multiplos de 3:")
for numero in range(1, 11):
    if numero % 3 == 0:
        continue
    print(numero)
