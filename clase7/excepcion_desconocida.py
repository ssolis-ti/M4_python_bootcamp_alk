#en este ejemplo, asumiremos que no conocemos el error ZeroDivision

while True:
    try:
        #intenta ejecutar esto
        numero = int(input("Ingresa un numero: ")) #python espera que el input venga con un numero para convertirlo en entero
        resultado = 10/numero
        print("Resultado", resultado)
        break


    except ValueError:
        print("El dato ingresado no es un numero valido")
        continue
     
    except Exception as e:
        print("Ocurrio un error con este mensaje", type(e), e)
        continue

