diccionarios = {
    "nombres": ["Juliana", "Julianita", "Julia", "Juli", "Julieta"],
    "telefonos": [3103271589, 3103211111, 3103222222, 3103233333, 3103244444]
}

print("Datos registrados:")
for nombre in diccionarios["nombres"]:
    print(nombre)
for telefono in diccionarios["telefonos"]:
    print(telefono)

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
