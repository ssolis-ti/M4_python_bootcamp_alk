"""¿En qué consistirá la Demo?
Vas a diseñar una clase que represente un producto de tienda, 
controlando el acceso y modificación del precio a través de métodos específicos.
🔹 Qué debe tener la clase:
Un atributo público para el nombre del producto
Un atributo privado para el precio (__precio)
Un método para ver el precio (getter)
Un método para modificar el precio (setter), que solo permita valores positivos
En el constructor (__init__), usar el setter para validar el precio desde el inicio
🔹 Qué se debe probar con objetos:
Crear un producto con precio válido
Mostrar el precio usando el getter
Intentar cambiar el precio a un valor negativo (debe mostrar un error)
Modificar correctamente el precio y verificar el nuevo valor
"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        # self.__precio = precio #Esto se saltaria las validaciones
        
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio> 0:
            self.__precio = precio
        else:
            raise  ValueError("El precio debe ser mayor a cero")
        
            # print("El precio debe ser mayor a cero")


# jamon = Producto("Jamon",-1000)
leche = Producto("Leche",1000)
print(leche.nombre)
print(leche.get_precio())

leche.set_precio(1800)
print("Nuevo precio ",leche.get_precio())
