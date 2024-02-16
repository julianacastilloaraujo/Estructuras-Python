def vocal(dato):
    vocales = "aeiou"
    return dato in vocales

dato = input("Ingrese el dato: ")

if len(dato) != 1:
    print("Por favor, ingrese un solo un dato.")
else:
    if vocal(dato):
        print("el dato ingresado es una vocal.")
    else:
        print("el dato ingresada no es una vocal.")