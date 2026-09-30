peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {round(imc, 2)}")