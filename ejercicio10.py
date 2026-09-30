payasos = int(input("Cuantos payasos quieres comprar: "))
munecas = int(input("Cuantas muñecas quieres comprar: "))
peso_payasos = payasos * 112
peso_munecas = munecas * 75
peso_total = peso_payasos + peso_munecas
cantidad_total = payasos + munecas
print(f"El peso total del paquete es: {peso_total} gramos y la cantidad total de productos es: {cantidad_total}")