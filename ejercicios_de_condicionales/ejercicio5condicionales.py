edad = int(input("Dime la edad que tienes: "))
ingresos = int(input("Dime tus ingresos mensuales: "))
if edad >= 16:
    if ingresos >= 1000:
        print("Puedes tributar")
    else:
        print("No puedes tributar")
else:
    print("No puedes tributar")
