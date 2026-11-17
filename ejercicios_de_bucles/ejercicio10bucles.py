
num = int(input("Introduce un número entero: "))

primo = True

if num < 2:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False

if primo:
    print("Es un número primo")
else:
    print("No es un número primo")
