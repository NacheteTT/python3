
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0

for i in frase:
    if i == letra:
        contador = contador + 1

print("La letra aparece", contador, "veces")
