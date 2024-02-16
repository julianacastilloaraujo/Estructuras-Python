SaldoInicial = 1000
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion=float(input("Seleccione una opción: "))
if opcion == 1:
        ingreso = float(input("Ingrese la cantidad de dinero: "))
        SaldoActual = ingreso + SaldoInicial
elif opcion == 2:
        retiro = float(input("Digite la cantidad a retirar: "))
        SaldoActual = SaldoInicial - retiro
elif opcion == 3:
        print(f"{SaldoInicial}")
        exit();
elif opcion == 4:
        exit();
print(SaldoActual)