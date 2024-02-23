diccionarios = { # carrera, nombre, id, email, icfes, telefono
  "carrera": ["Ingeniería de Sistemas", "Contabilidad", "Administracion"],
  "nombre": ["Juliana", "Ivan", "Cristian"],
  "id": [12345, 56789, 10112],
  "email": ["juliana@gmail.com","ivan@gmail.com", "cristian@gmail.com"],
  "icfes": [300, 400, 500],
  "telefono": [3103271589, 3103211111, 3103222222]
}

print("Datos registrados:")
for carrera, nombre, id, email, icfes, telefono in diccionarios.items():
    print("Carrera: {carrera} Nombre: {telefono} ID: {id} Email: {email} ICFES: {icfes} Teléfono: {telefono}")

print("\nNúmeros de teléfono registrados:")
for telefono in diccionarios["telefonos"]:
  print(telefono)

nombre_consulta = input("Ingrese el nombre de la persona para consultar su número de teléfono: ")
if nombre_consulta in diccionarios["nombres"]:
  index = diccionarios["nombres"].index(nombre_consulta)
  telefono = diccionarios["telefonos"][index]
  print(f"El número de teléfono de {nombre_consulta} es: {telefono}")
else:
  print("La persona no está registrada.")

total_personas = len(diccionarios["nombres"])
print(f"\nTotal de personas registradas: {total_personas}")
