""" Objetivo funcional:

Solicitar un número entero
Detectar si el usuario escribe texto o caracteres inválidos
Mostrar un mensaje amigable en lugar de un traceback

🔹 Variantes para probar:
Ingresar "25" → ✅ válido
Ingresar "abc" → ❌ ValueError
Ingresar "10.5" → ❌ ValueError (por ser float)
"""
# try:
#     numero = int(input("Ingrese un un numero :"))
#     print("Felicidades el numero es correcto")
# except ValueError:
#     print("El valor ingresado no es correcto")


#variante mas fina (validacion)


while True:
    entrada = input("Ingrese un un numero :")

    try:
        numero = int(entrada)
        print("Felicidades el numero es correcto")
    except ValueError:
        
        try:
            numero = float(entrada)
            print("El valor ingrado es un numero decimal, favor intentar con un entero")
        except ValueError:
            print("El valor ingresado no es valido")