def multiplicacion(x, y):
    return x * y

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def division(x, y):
    if y == 0:
        # Es mejor lanzar una excepción para que el código que llama pueda manejarla.
        return "Error: División por cero no es permitida."
    else:
        return x / y
