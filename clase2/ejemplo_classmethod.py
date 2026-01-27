class Libro:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    @classmethod
    def con_descuento(cls, titulo,precio):
        precio_final = precio * 0.8
        return cls(titulo,precio_final)
    

libro1 = Libro("Python para todos",10000)
libro2 = Libro.con_descuento("Python volumen2",10000)

print(libro1.precio) #10000
print(libro2.precio) #8000