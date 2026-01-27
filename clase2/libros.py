"""Definir la clase Libro con los atributos titulo, autor, anio
Agregar un método mostrar_info() que imprima todos los datos
Crear dos objetos Libro diferentes
Llamar al método mostrar_info() de cada objeto

📌 Objetivo: reforzar cómo se usan múltiples atributos, cómo funcionan los métodos,
 y cómo crear varios objetos con datos distintos.
"""

class Libro:

    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    
    def mostrar_info(self):

        print(f"""
                Titulo: {self.titulo}
                Autor: {self.autor}
                Año: {self.anio}
            """)

libro1 = Libro("Cien años de soledad","Gabriel Garcia Marquez", 1967)
libro2 = Libro("Clean Code","Robert C. Martin", 2008)
libro3 = Libro("Harry Potter y la piedra filosofal","J K Rowling", 1997)
libro4 = Libro("¿Sueñan los androides con ovejas eléctricas?","Philip K. Dick", 1968)

libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()
libro4.mostrar_info()

libro4.titulo = "La vaca lola"

libro4.mostrar_info()
