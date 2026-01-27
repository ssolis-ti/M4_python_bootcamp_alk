class Persona:
    def __init__(self, nombre, edad, rut):
        self.nombre = nombre     #publico
        self._edad = edad        #protegido
        self.__rut = rut         #privado

yo = Persona("Jose", 34, "17942994-2")

print(yo.nombre)
# yo._edad = 10
# print(yo._edad)
## la accion realizada anteriormente, no constituye buenas practicas en python,
#por que los atributos con 1 guion bajo o protegidos solo deben usarse dentro de su propia clase
#Sin embargo Python no bloquea la modificacion externa
print(yo.__rut) #esto arroja un error