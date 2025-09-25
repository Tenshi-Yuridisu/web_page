def multiplicacion(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x * y

def suma(x, y):
    if x == 0 or y == 0:
        return x + y
    else:
        return x + y
def resta(x, y):
    if x == 0 or y == 0:
        return x - y
    else:
        return x - y
def division(x, y):
    if y == 0:
        return "Error: División por cero no es permitida."
    else:
        return x / y

while True:
    print("\nSeleccione una operación:")
    print("1. Multiplicación")
    print("2. Suma")
    print("3. resta")
    print("4. dividir")
    print("5. Salir")
    print("Nota: Ingrese solo números enteros.")

    opcion = input("Ingrese la opción (1/2/3): ")

    if opcion == '1' or opcion == '2':
        try:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese otro numero: "))
            if opcion == '1':
                print(f"El resultado de la multiplicación es: {multiplicacion(x, y)}")
            elif opcion == '2':
                print(f"El resultado de la suma es: {suma(x, y)}")
            elif opcion == '3':
                print(f"el resultado de la resta es: {resta(x,y)}")
            elif opcion == '4':
                print(f"el resultado de la division es: {division(x,y)}")
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
