carreras = ("Zootecnia", "Ingenieria de sistemas y computación", "Contabilidad", "Administración de empresas")
Aspirantes = {}

def Agregar_Aspirantes():
    Nombre = input("Ingrese su nombre completo: ")
    Dni = input("Ingrese el número de documento de identidad: ")
    Email = input("Ingrese su dirección de correo electrónico: ")
    Score_icfes = input("Ingrese su puntaje en el ICFES: ")
    Numero_Telefonico = input("Ingrese su número telefónico: ")

    for i, carrera in enumerate(carreras):
        print(f"{i + 1}. {carrera}")
    opcion_carrera = int(input("Seleccione la carrera que desea: "))
    opcionSeleccionada = carreras[opcion_carrera - 1]

    Persona = {"Nombre": Nombre, "Dni": Dni, "Email": Email, "Score_icfes": Score_icfes,
               "Numero_Telefonico": Numero_Telefonico, "Carrera_Seleccionada": opcionSeleccionada}
    Aspirantes[Nombre] = Persona
    print(f"{Nombre} ha sido registrado como aspirante en la carrera de {opcionSeleccionada}.\n")

def MostrarDatosAspirante():
    Nombre = input("Ingrese el nombre del aspirante a buscar: ")
    if Nombre in Aspirantes:
        print("\nDatos del Aspirante:")
        print(f"Nombre: {Aspirantes[Nombre]['Nombre']}")
        print(f"DNI: {Aspirantes[Nombre]['Dni']}")
        print(f"Email: {Aspirantes[Nombre]['Email']}")
        print(f"Score ICFES: {Aspirantes[Nombre]['Score_icfes']}")
        print(f"Número Telefónico: {Aspirantes[Nombre]['Numero_Telefonico']}")
        print(f"Carrera Seleccionada: {Aspirantes[Nombre]['Carrera_Seleccionada']}\n")
    else:
        print(f"No se encontró a {Nombre} en la lista de aspirantes.\n")

def EliminarDatos():
    Nombre = input("Ingrese el nombre del aspirante a eliminar: ")
    if Nombre in Aspirantes:
        print(f"\nDatos del Aspirante a Eliminar:")
        print(f"Nombre: {Aspirantes[Nombre]['Nombre']}")
        print(f"DNI: {Aspirantes[Nombre]['Dni']}")
        print(f"Email: {Aspirantes[Nombre]['Email']}")
        print(f"Score ICFES: {Aspirantes[Nombre]['Score_icfes']}")
        print(f"Número Telefónico: {Aspirantes[Nombre]['Numero_Telefonico']}")
        print(f"Carrera Seleccionada: {Aspirantes[Nombre]['Carrera_Seleccionada']}\n")

        confirmacion = input("¿Está seguro de eliminar estos datos? (Sí/No): ")
        if confirmacion.lower() == 'si':
            del Aspirantes[Nombre]
            print(f"\nDatos del aspirante {Nombre} eliminados exitosamente.\n")
        else:
            print("Operación cancelada.\n")
    else:
        print(f"No se encontró a {Nombre} en la lista de aspirantes.\n")

while True:
    print("1. Registrar aspirante")
    print("2. Mostrar Datos")
    print("3. Eliminar Datos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Agregar_Aspirantes()
    elif opcion == "2":
        print("Las carreras con las que cuenta la Universidad de Cundinamarca son\n",carreras)
        MostrarDatosAspirante()
    elif opcion == "3":
        EliminarDatos()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Ingrese un número válido.\n")