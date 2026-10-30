cant = float(input("Dime que cantidad quieres invertir: "))
anio = int(input("Dime cuantos años quieres invertir: "))
anual = float(input("Dime con que interes en numero Ej. 3% => 3: "))

interes = anual/100

for i in range(anio):
    ganancia = cant * interes
    cant = cant + ganancia
    print(f"En el año {i+1} ya tienes {cant:.2f} €")