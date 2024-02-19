productos = (
    ("alimenticio", ("Leche", "Pan", "Frutas", "Verduras", "Huevos", "Carne", "Arroz")),
    ("aseo", ("Jabón", "Detergente", "Champú", "Crema dental", "Papel higiénico")),
    ("licor", ("Cerveza", "Vino", "Whisky", "Ron"),
     "electrodomesticos", ("Celular", "Televisor", "Nevera", "Lavadora", "Computador")),
)

productos_usuario = []

def agregar_producto(producto, tipo):
    tipo_encontrado = next((categoria for categoria, _ in productos if categoria == tipo), None)
    if tipo_encontrado:
        lista_productos = next((lista for categoria, lista in productos if categoria == tipo), [])
        if producto in lista_productos:
            productos_usuario.append(producto)
            print(f"Producto '{producto}' agregado al carrito.")
        else:
            print(f"El producto '{producto}' no está en la lista de productos {tipo}.")
    else:
        print(f"El tipo de producto '{tipo}' no es válido.")

def buscar_producto(producto):
    categoria = next((categoria for categoria, lista in productos if producto in lista), None)
    if categoria:
        print(f"El producto '{producto}' está en la lista de productos {categoria.capitalize()}.")
    else:
        print(f"El producto '{producto}' no está en la lista general.")

def eliminar_producto(producto):
    if producto in productos_usuario:
        productos_usuario.remove(producto)
        print(f"Producto '{producto}' eliminado.")
    else:
        print(f"El producto '{producto}' no está en el carrito.")

def mostrar_productos():
    print("Lista de productos:")
    for categoria, lista_productos in productos:
        print(f"{categoria.capitalize()}:")
        for producto in lista_productos:
            print(f"- {producto}")

def mostrar_carrito():
    print("Carrito de compra:")
    for producto in productos_usuario:
        print(f"- {producto}")

def menu():
    while True:
        print("""
        Opciones:
        1. Agregar producto
        2. Buscar producto
        3. Eliminar producto
        4. Mostrar productos
        5. Mostrar carrito
        6. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            tipo = input("Ingrese el tipo de producto (alimenticio, aseo, licor, electrodomesticos): ").lower()
            producto = input("Ingrese el nombre del producto: ").capitalize()
            agregar_producto(producto, tipo)
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto a buscar: ").capitalize()
            buscar_producto(producto)
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto a eliminar: ").capitalize()
            eliminar_producto(producto)
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "5":
            mostrar_carrito()
        elif opcion == "6":
            print("Gracias")
            break
        else:
            print("Opcion incorrecta")

menu()
