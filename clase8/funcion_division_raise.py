
def division(a,b):
    if b == 0 :
        raise ZeroDivisionError("No se puede dividir por 0!!!!")
    return a/b

print(division(9,1))