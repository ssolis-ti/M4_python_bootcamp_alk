"""🔹 Lo que deberá tener la clase:
Atributos públicos como nombre y salario
Un atributo de clase llamado aumento_general con un valor inicial (ej. 1.05)
Un método de clase que permita modificar el porcentaje de aumento general para todos los empleados
Un método estático que reciba un salario y verifique si supera un cierto umbral (ej. sueldo mínimo)
🔹 Qué se debe probar:
Crear varios empleados con salarios distintos
Modificar el aumento general desde la clase
Usar el método estático para evaluar si un salario es alto o bajo
Ver cómo el método de clase afecta a todos los objetos
"""

class Empleado:
    
    #atributo de clase
    aumento_general = 1.05
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @classmethod
    def cambio_aumento(cls, nuevo_aumento):
        if nuevo_aumento >1:
            cls.aumento_general = nuevo_aumento
        else:
            raise ValueError("Aumento no valido")
    
    @staticmethod
    def supera_sueldo_minimo(salario):
        SUELDO_MINIMO = 539000
        return salario >= SUELDO_MINIMO
    

empleado1 = Empleado("Diego", 600000)
empleado2 = Empleado("Juan", 600000)
print(empleado1.aumento_general)
print(empleado2.aumento_general)

Empleado.cambio_aumento(2.00)

print(empleado1.aumento_general)
print(empleado2.aumento_general)


print(empleado2.supera_sueldo_minimo(600000))
