sexo = input("Di m si eres hombre y f si eres mujer: ")
letra = input("Di la primera letra de tu nombre: ")
if sexo == "f":
    if letra <= "m":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
elif sexo == "m":
    if letra >= "n":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
else:
    print("Error debes decir m o f en la eleccion de genero")
