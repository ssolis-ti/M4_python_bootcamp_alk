
class Cuenta:
    def __init__(self):
        self.__saldo = 0

    #metodos accesadores
    #getter
    def get_saldo(self):
        return self.__saldo
    
    #setter 
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = self.__saldo + nuevo_saldo
        
cuenta1 = Cuenta()
# print(cuenta1.__saldo)#esto no es posible
print(cuenta1.get_saldo())
cuenta1.set_saldo(-500)
print(cuenta1.get_saldo())
cuenta1.set_saldo(500)
print(cuenta1.get_saldo())
cuenta1.set_saldo(500000)
print(cuenta1.get_saldo())
