
def validar_email(email):
    if '@' not in email:
        raise ValueError("Email invalido")
    

#para python un texto puede ser considerado un iterable
email = "pepe112@gmail.com"
#'@' in email -> para python es como si fuera ['p','e','p','e','1','1','2','@','g','m','a','i','l','.',c','o','m']

def registrar_usuario(email):
    try:
        validar_email(email)
    except ValueError as e:
        print("error interno: ", e)
        raise



try:
    registrar_usuario("usuario_sin_arroba.com")
except ValueError:
    print("Error detectado en el sistema externo:reintenta con un email valido")