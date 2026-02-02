"""probar 1 ingresar un 0
2. ingresar un texto #ValueError
3."""

while True:
    try:
        #intenta ejecutar esto
        numero = int(input("Ingresa un numero: ")) #python espera que el input venga con un numero para convertirlo en entero
        resultado = 10/numero
        print("Resultado", resultado)
        break
    except ZeroDivisionError:
        print("Error no se puede dividir por 0")
        continue

    except ValueError:
        print("El dato ingresado no es un numero valido")
        continue

    except KeyboardInterrupt:
        print("Se detuvo la ejecucion manualmente Adios")
        print("Saliendo....")
        break