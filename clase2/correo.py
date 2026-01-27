class CuentaCorreo:
    def __init__(self, correo, contrasenna, nombre_de_usuario):
        self.correo = correo #publico
        self._nombre_de_usuario = nombre_de_usuario #protegido
        self.__contrasenna = contrasenna  #privado