pan_otro_dia = int(input("Cuantas barras de pan se han vendido de otro dia hoy: "))
precio_pan = 3.49*pan_otro_dia
descuento_pan = 0.60*precio_pan
precio_final = precio_pan - descuento_pan
print(f"Si el pan vendido hubiera sido del dia habria costado: {round(precio_pan, 2)}€")
print(f"El descuento aplicado es de: {round(descuento_pan, 2)}€")
print(f"El precio final es de: {round(precio_final, 2)}€")