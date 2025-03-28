# Hola
entero = 10 # int

flotante = 10.7 # float

verdadero = True
falso = False

vacio = None

cadena_texto = "Hola, esto es una cadena de texto." # str

cadena_texto2 = 'Hola, esto tambien es una cadena de texto' # str

ejemplo = "' esto es una comilla simple"

ejemplo2 = ' " esto es una comilla doble'

ejemplo3 = " \"" # escapearla con \

ejemplo4 = "Salto\nlinea"


lista = [1,2]
tupla = 2, 3


lista.append(1)
lista.pop(0)
lista.remove(1)


valor = ()
valor2 = tuple()

diccionario = {}

diccionario2 = {
    "clave": 1
}

# conjuntos sirve para no tener duplicados
conjunto = set() # set

def foo(valor=None):
    valor = valor or []
    valor.append(1)
    return valor


def foo(valor=None):
    if valor is None:
        valor = []
    valor.append(1)
    return valor


def foo(valor=None):

    valor = valor or []

    for i in range(20):
        valor.append(i)
    return valor


valor = 0

print(valor or 1)