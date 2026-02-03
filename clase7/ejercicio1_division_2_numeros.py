

"""Creá una función que:
Pida al usuario dos números
Intente dividir el primero por el segundo
Maneje dos errores posibles:
Entrada inválida (ValueError)
División por cero (ZeroDivisionError)
Imprima mensajes personalizados para ca
"""


def division_dos_numeros():
    print("bienvenido al programa para dividir (dividendo/divisor)")
   
    

    try:
        numero_1 = float(input("Ingrese el dividendo(primer numero): "))
    except ValueError:
        print("valor dividendo no valido")
        return #esto detiene la funcion
        

    try:
        numero_2 = float(input("Ingrese el divisor (segundo numero): "))
    except ValueError:
        print("valor divisor no valido")    
        return
    try:    
        cociente = numero_1/numero_2
        print("Resultado de la division: ", cociente)

    except ZeroDivisionError:
        print("el divisor no puede ser igual a cero")
        



division_dos_numeros()