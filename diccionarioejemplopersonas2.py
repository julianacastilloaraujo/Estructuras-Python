diccionarios = {
  "nombres": ["Juliana", "Julianita", "Julia", "Juli", "Julieta"],
  "telefonos": [3103271589, 3103211111, 3103222222, 3103233333, 3103244444]
}

print("Datos registrados:")
for nombre, telefono in diccionarios.items():
    print("Nombre: {nombre}, Teléfono: {telefono}")

while True:
    agregar = input("\n¿Deseas agregar una nueva persona? (si/no): ")
    if agregar.lower() != 'si':
        break
    
    nuevonombre = input("Ingrese el nombre de la persona: ")
    nuevotelefono = input("Ingrese el teléfono de la persona: ")
    
    diccionarios["nombres"].append(nuevonombre)
    diccionarios["telefonos"].append(nuevotelefono)

print("\nDatos registrados actualizados:")
for nombre, telefono in zip(diccionarios["nombres"], diccionarios["telefonos"]):
    print(f"Nombre: {nombre}, Teléfono: {telefono}")

nombre_consulta = input("\nIngrese el nombre de la persona para consultar su número de teléfono: ")
if nombre_consulta in diccionarios["nombres"]:
    index = diccionarios["nombres"].index(nombre_consulta)
    telefono = diccionarios["telefonos"][index]
    print(f"El número de teléfono de {nombre_consulta} es: {telefono}")
else:
    print("La persona no está registrada.")

total_personas = len(diccionarios["nombres"])
print(f"\nTotal de personas registradas: {total_personas}")
