def mi_decorador(funcion):
    def envoltura():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return envoltura


@mi_decorador
def saludar():
    print("Hola")

saludar()

