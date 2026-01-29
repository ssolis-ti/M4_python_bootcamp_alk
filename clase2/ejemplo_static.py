####static method

class Libro:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    @staticmethod
    def es_precio_valido(precio):
        return precio> 0
    
    @staticmethod
    def calcular_iva(precio):
        return precio * 0.19
    
# print(Libro.es_precio_valido(-1000))
# print(Libro.es_precio_valido(1000))

libro1 = Libro("Harry potter 1",1000)
print(libro1.calcular_iva(1000))

print(Libro.calcular_iva(10000))