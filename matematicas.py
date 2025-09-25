def multiplicacion(x, y):
    if x == 0 or y == 0:
        # Es mejor devolver el resultado numérico, ya que 0 es un resultado válido.
        # La validación de entrada debe hacerse antes de llamar a la función.
        return 0
    else:
        return x * y

def suma(x, y):
    if x == 0 or y == 0:
        # Similar a la multiplicación, 0 es un sumando válido.
        return x + y
    else:
        return x + y

while True:
    print("\nSeleccione una operación:")
    print("1. Multiplicación")
    print("2. Suma")
    print("3. Salir")

    opcion = input("Ingrese la opción (1/2/3): ")

    if opcion == '1' or opcion == '2':
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese otro numero: "))
        if opcion == '1':
            print(f"El resultado de la multiplicación es: {multiplicacion(x, y)}")
        elif opcion == '2':
            print(f"El resultado de la suma es: {suma(x, y)}")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
