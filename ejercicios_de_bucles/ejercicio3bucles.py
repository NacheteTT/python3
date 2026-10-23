num = int(input("Di un número entero positivo: "))

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i, end=", ")
