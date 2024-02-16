def vocal(letra):
    vocales = "aeiou"
    return letra in vocales

letra = input("Ingrese el dato: ")

if len(letra) != 1:
    print("Por favor, ingrese un solo un dato.")
else:
    if vocal(letra):
        print("el dato ingresado es una vocal.")
    else:
        print("el dato ingresada no es una vocal.")