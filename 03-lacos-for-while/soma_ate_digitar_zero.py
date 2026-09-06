total_sum = 0
print("coloque os numeros na soma. digite 0 para terminar a soma.")

while True:
    try:
        num_str = input("coloque um numero: ")
        num = int(num_str)
        if num == 0:
            break
        total_sum += num
    except ValueError:
        print("input invalido. por favor coloque outro numero.")

print(f"a soma final é: {total_sum}")
