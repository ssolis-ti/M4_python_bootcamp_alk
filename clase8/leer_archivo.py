try:
    archivo = open('info.txt','r')
    print(archivo.read())

except FileNotFoundError:
    print("Archivo no encontrado ....")

else:
    print("TODO FUNCIONA CORRECTAMENTE!!!!")

finally:
    try:
        archivo.close()
        print("Cerrando recursos....")
    
    except NameError:
        print("Archivo no creado, cerrando programa")
    