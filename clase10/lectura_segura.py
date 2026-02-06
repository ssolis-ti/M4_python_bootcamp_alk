
with open('avengers.txt') as archivo:
    print(archivo.read())

    print(archivo.closed)

    #podemos observar que el archivo se cierra automaticamente justo antes de la ultima linea del bloque