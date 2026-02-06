import os
print("El archivo a ser leido debe encontrarse en la carpeta de este script")
ruta = input("Ingrese el nombre del archivo con su extension(.txt,.log,.json, etc): ")

try:
    archivo = open(ruta, 'r')
    print("Nombre del archivo: ",archivo.name)
    
    
        
except FileNotFoundError:
    print(f"archivo no encontrado, revise su ruta")
except Exception as e:
    print("Se detecto otro error:" , e)

# else:
#     print("Intentamos cerrar el archivo")

#     if not archivo.closed:
#         archivo.close()
#         print("El archivo se cerro correctamente")

finally:
    try:
        archivo.close()
        print("Cerrando el script")
    except NameError:
        print("Archivo no encontrado.....")
        print("Saliendo del script...")