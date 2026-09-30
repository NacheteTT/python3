cant = int(input("Di la cantidad que quieres invertir: "))
interes = float(input("Di el interes anual (en porcentaje): "))
anios = int(input("Di el numero de años que quieres invertir: "))
interes_decimal = interes / 100
resultado = cant * (1 + interes_decimal) ** anios
capital_final = round(resultado, 2)
print(f"El capital final es: {capital_final}")