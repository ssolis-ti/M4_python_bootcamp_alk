


class ErrorAplicacion(Exception):
        pass

class ErrorValidacion(ErrorAplicacion):
        pass

class ErrorPermisos(ErrorAplicacion):
        pass


def verificar_usuario(rol):
        
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado")
        
    elif rol not in ["admin","editor"]:
        raise ErrorValidacion("Rol invalido")
    

try:
    verificar_usuario("visitante")

except ErrorPermisos:
      print("Error: no tienes permisos suficientes")
except ErrorValidacion:
      print("Error: datos invalidos")

except ErrorAplicacion:
      print("Otro error general de la aplicacion")