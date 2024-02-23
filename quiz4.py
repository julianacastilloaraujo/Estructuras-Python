def mostrar_menu():
  print("Registro de Personas")
  print("1. Mostrar todos los datos de los estudiantes")
  print("2. Ingresar un nuevo estudiante")
  print("3. Editar datos")
  print("4. Salir")

carreras = ("Ingeniería", "Contabilidad", "Administración", "Zootecnia")

diccionarios = {
  "nombres": ["Juliana", "Julianita", "Julia", "Juli"],
  "carrera": ["ingenieria", "contabilidad", "administracion", "zootecnia"],
  "telefonos": [3103271589, 3103211111, 3103222222, 3103233333],
  "puntaje_icfes": [300, 400, 500, 600],
  "correos": ["juliana@gmail.com","julianita@gmail.com","julia@gmail.com", "juli@gmail.com"]
}

while True:
  mostrar_menu()
  opcion = int(input("Seleccione una opción: "))

  if opcion == 1:
    for nombre, carrera, telefonos, puntaje_icfes, correo in zip(diccionarios["nombres"], diccionarios["carrera"], diccionarios["telefonos"], diccionarios["puntaje_icfes"], diccionarios["correos"]):
      print(f"Nombre: {nombre}, Carrera: {carrera}", f"Telefono: {telefonos}", f"Puntaje ICFES: {puntaje_icfes}", f"Correo: {correo}")

  elif opcion == 2:
    nuevonombre = input("Ingrese el nombre de la persona: ")

    print("Seleccione la carrera:")
    for i, carrera in enumerate(carreras):
      print(f"{i + 1}. {carrera}")
    opcion_carrera = int(input("Ingrese el número de la carrera: "))
    nuevocarrera = carreras[opcion_carrera - 1]

    nuevotelefono = input("Ingrese el teléfono de la persona: ")
    nuevopuntaje_icfes = input("Ingrese el puntaje ICFES de la persona: ")
    nuevocorreo = input("Ingrese el correo de la persona: ")

    diccionarios["nombres"].append(nuevonombre)
    diccionarios["carrera"].append(nuevocarrera)
    diccionarios["telefonos"].append(nuevotelefono)
    diccionarios["puntaje_icfes"].append(nuevopuntaje_icfes)
    diccionarios["correos"].append(nuevocorreo)

    print("Persona agregada correctamente.")

  elif opcion == 3:
    nombre_editar = input("Ingrese el nombre de la persona a editar: ")

    if nombre_editar in diccionarios["nombres"]:
      index = diccionarios["nombres"].index(nombre_editar)

      print("Seleccione la nueva carrera:")
      for i, carrera in enumerate(carreras):
        print(f"{i + 1}. {carrera}")
      opcion_carrera = int(input("Ingrese el número de la carrera: "))
      nuevo_carrera = carreras[opcion_carrera - 1]

      nuevo_telefono = input("Ingrese el nuevo teléfono: ")
      nuevo_puntaje_icfes = input("Ingrese el nuevo puntaje ICFES: ")
      nuevo_correo = input("Ingrese el nuevo correo: ")

      diccionarios["carrera"][index] = nuevo_carrera
      diccionarios["telefonos"][index] = nuevo_telefono
      diccionarios["puntaje_icfes"][index] = nuevo_puntaje_icfes
      diccionarios["correos"][index] = nuevo_correo

      print("Datos actualizados correctamente.")
    else:
      print("La persona no está registrada.")

  elif opcion == 4:
    break

  else:
    print("Opción no válida.")
