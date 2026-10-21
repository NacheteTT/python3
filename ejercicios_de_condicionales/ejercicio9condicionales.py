edad = int(input("Dime la edad que tienes: "))
if edad < 4:
    print("Tienes entrada gratis")
elif edad >= 4 and edad <= 18:
    print("Tu entrada cuesta 5 euros")
elif edad > 18:
    print("Tu entrada cuesta 10 euros")
