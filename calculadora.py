import math

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b==0:
        return 'Error: no se puede dividir entre cero'
    else:
        return a/b
    
def potencia(a,b):
    return a**b

def raiz_cuadrada(a):
    if a < 0:
        return 'Error: no se puede calcular la raíz cuadrada de un numero negativo'
    else:
        return match.sqrt(a)
    
def operaciones(signo,a,b=None):
    if