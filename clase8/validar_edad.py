"""🔹 Objetivo funcional:

Controlar que la edad sea un número positivo
Lanzar una excepción con un mensaje personalizado si no se cumple

🔹 Pasos esperados:

Definí una función validar_edad(edad)
Usá raise ValueError("La edad no puede ser negativa") si la edad es menor a 0
Si la edad es válida, imprimí un mensaje como “Edad válida: X años”
Probalo con validar_edad(25) y luego con validar_edad(-3)
"""

#vamos a crear nuestro propio error

class EdadInvalidaError(Exception):
    pass



def validar_edad(edad):
    
    try:
        # edad = int(edad)
        if not isinstance(edad, int):
            raise EdadInvalidaError("La edad ingresada no es un numero entero")
        
    except ValueError:
        raise ValueError("La edad ingresada  no es un valor valido")

    if edad < 0:
        raise ValueError("La edad ingresada no puede ser un valor negativo")
    print("Edad validad correctamente")
    
# validar_edad(-3)
# validar_edad('uno')
validar_edad("25")
# validar_edad(23)