puntuacion = float(input("Diga su puntuacion: "))
suma = 2400 * puntuacion
total = 2400 + suma

if puntuacion == 0.0:
    print(f"Tu puntuacion es inaceptable y tu sueldo es {total}")
elif puntuacion == 0.1:
    print(f"Tu puntuacion es inaceptable y tu sueldo es {total}")
elif puntuacion == 0.2:
    print(f"Tu puntuacion es inaceptable y tu sueldo es {total}")
elif puntuacion == 0.3:
    print(f"Tu puntuacion es inaceptable y tu sueldo es {total}")
elif puntuacion == 0.4:
    print(f"Tu puntuacion es aceptable y tu sueldo es {total}")
elif puntuacion == 0.5:
    print(f"Tu puntuacion es aceptable y tu sueldo es {total}")
elif puntuacion >= 0.6:
    print(f"Tu puntuacion es meritorio y tu sueldo es {total}")
else:
    print("La puntuación introducida no es válida.")