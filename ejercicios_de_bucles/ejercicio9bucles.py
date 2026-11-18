contrasena = "contraseña"
usuario = input("Introduce la contraseña: ")

while usuario != contrasena:
    usuario = input("Contraseña incorrecta. Inténtalo de nuevo: ")

print("Contraseña correcta. Acceso permitido.")