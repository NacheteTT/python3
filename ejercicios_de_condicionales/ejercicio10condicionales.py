print("En la Pizzeria Bella Napoli ofecemos dos tipos de pizzas")
tippizza = input("Que tipo de pizza quieres Vegetariana o No Vegetariana: ")
if tippizza == "vegetariana":
    print("Para las pizzas Vegetarianas tenemos dos ingredientes a escoger")
    ingrediente1 = input("Que quieres añadir Pimiento o Tofu? ")
    print(f"Ha elegido una pizza Vegetariana y con el ingrediente {ingrediente1}")
elif tippizza == "no vegetariana":
    print("Para las pizzas No vegetarianas tenemos tres ingredientes a escoger")
    ingrediente2 =input("Que quieres añadir Peperoni, Jamon o Salmon? ")
    print(f"Ha elegido una pizza No vegetariana y con el ingrediente {ingrediente2}")