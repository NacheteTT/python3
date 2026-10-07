compra = input("Di los productos de tu lista de la compra separados por comas: ")
productos = compra.split(",")
for producto in productos:
    print(producto.strip())