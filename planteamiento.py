# Lista de carreras disponibles
carreras = ("Ingeniería de Sistemas", "Derecho", "Medicina", "Administración de Empresas", "Psicología")

# Diccionario para la información de cada aspirante
aspirante = {
    "nombre": "",
    "documento": "",
    "correo": "",
    "puntaje_icfes": 0,
    "telefono": "",
    "carrera": "",
}

# Lista para almacenar la información de todos los aspirantes
aspirantes = []

# Función para registrar un nuevo aspirante
def registrar_aspirante():
    # Pedir la información del aspirante
    aspirante["nombre"] = input("Ingrese su nombre: ")
    aspirante["documento"] = input("Ingrese su número de documento: ")
    aspirante["correo"] = input("Ingrese su correo electrónico: ")
    aspirante["puntaje_icfes"] = int(input("Ingrese su puntaje ICFES: "))
    aspirante["telefono"] = input("Ingrese su número de teléfono: ")
    
    # Mostrar las carreras disponibles
    for i, carrera in enumerate(carreras):
        print(f"{i + 1}. {carrera}")
    
    # Seleccionar la carrera
    opcion_carrera = int(input("Seleccione la carrera que desea: "))
    aspirante["carrera"] = carreras[opcion_carrera - 1]
    
    # Agregar el aspirante a la lista
    aspirantes.append(aspirante.copy())

# Función para mostrar la información de un aspirante
def mostrar_aspirante(indice):
    aspirante = aspirantes[indice]
    print(f"Nombre: {aspirante['nombre']}")
    print(f"Documento: {aspirante['documento']}")
    print(f"Correo electrónico: {aspirante['correo']}")
    print(f"Puntaje ICFES: {aspirante['puntaje_icfes']}")
    print(f"Teléfono: {aspirante['telefono']}")
    print(f"Carrera: {aspirante['carrera']}")

# Función para eliminar la información de un aspirante
def eliminar_aspirante(indice):
    del aspirantes[indice]

# Función para mostrar el menú principal
def mostrar_menu():
    print("-" * 20)
    print("Registro de Aspirantes")
    print("-" * 20)
    print("1. Registrar nuevo aspirante")
    print("2. Ver información de un aspirante")
    print("3. Eliminar información de un aspirante")
    print("4. Salir")
    print("-" * 20)

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        registrar_aspirante()
    elif opcion == 2:
        if not aspirantes:
            print("No hay aspirantes registrados.")
        else:
            indice = int(input("Ingrese el índice del aspirante que desea ver: ")) - 1
            if 0 <= indice < len(aspirantes):
                mostrar_aspirante(indice)
            else:
                print("Índice no válido.")
    elif opcion == 3:
        if not aspirantes:
            print("No hay aspirantes registrados.")
        else:
            indice = int(input("Ingrese el índice del aspirante que desea eliminar: ")) - 1
            if 0 <= indice < len(aspirantes):
                eliminar_aspirante(indice)
                print("Aspirante eliminado correctamente.")
            else:
                print("Índice no válido.")
    elif opcion == 4:
        break
    else:
        print("Opción no válida.")

# Ejemplo de uso
registrar_aspirante()
registrar_aspirante()
mostrar_aspirante(0)
eliminar_aspirante(1)
mostrar_aspirante(0)
