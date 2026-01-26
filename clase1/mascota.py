"""Consigna: ✍️
Creá una clase Mascota con:
Atributos: nombre, edad, tipo
Método presentarse() que diga "Soy {nombre}, un/a {tipo} de {edad} años."
Método es_joven() que devuelva True si tiene menos de 5 años

Paso a paso: ⚙️
Definí la clase y sus métodos

Creá una lista de 3 o más mascotas

Recorrelas con un for y:

Mostrá su presentación

Indicá si es joven o no

Bonus: Filtrá solo las mascotas jóvenes en una nueva lista

"""

class Mascota:

    #funcion de inicializacion de la clase
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    #declaramos los metodos de la clase(acciones)
    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")
        return #lo dejamos vacio por que no nos piden retornar nada, pero asi explicitamente sabermos que la funcion termina aqui
    
    def es_joven(self):
        # condicion = self.edad <5
        return self.edad < 5 #como es una condicion devuleve True si self.edad es menor a 5
    

perro = Mascota("Cachupin",15,"Perro")
gato = Mascota("Bola de nieve",4,"Gato")
loro = Mascota("Carlos Alberto",5,"Loro")
conejo = Mascota("Bugs", 3, "Conejo")

mascotas = [perro, gato, loro, conejo]
mascota_joven = []

for mascota in mascotas:
    mascota.presentarse()
    print("Es joven",mascota.es_joven())

    if mascota.es_joven():
        mascota_joven.append(mascota)



for joven in mascota_joven:
    print(joven.nombre)
