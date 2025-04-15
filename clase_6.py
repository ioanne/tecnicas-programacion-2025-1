
# Estandar
lista_alumnos = [
    {
        "id": 1, "valor": {"nombre": "Juan"}
    },
    {
        "id": 2, "valor": {"nombre": "Pedro"}
    },
    {
        "id": 3, "valor": {"nombre": "Maria"}
    }
]

# Bucle


diccionario_alumnos = {
    1: {"nombre": "Juan"},
    2: {"nombre": "Pedro"},
    3: {"nombre": "Maria"},
}

# Accedemos al valor de un diccionario, si no lo encuentra falla.
alumno = diccionario_alumnos[1]


# Accedemos al valor de un diccionario, si no lo encuentra devuelve None
alumnos2 = diccionario_alumnos.get(1)


lista_2 = [1, 2, 3, 4, 5]

1 in lista_2 # True
7 in lista_2 # False


"o" in "Hola" # True

"z" in "Hola" # False


for numero in [1, 2, 3, 4, 5]: # 1      2       3
    print(numero)


for clave, valor in {"a": "z"}.items():
    print(clave)
    print(valor)


diccionario = {1:2, 3:4}

# Convertir un diccionario en un objeto iterable
# Podemos acceder a los metodos keys, values e items.
claves_de_un_diccionario = diccionario.keys()
valores_de_un_diccionario = diccionario.values()
diccionario_iterable = diccionario.items() # (clave, valor)


# funciones / métodos por convención van en minusculas
diccionario.keys


def foo():
    return "Hola"


while True:
    print("Hola")

""" Palabras reservadas """

# Booleanos 
True # Siempre es con T mayuscula
False # Siempre es con F mayuscula


# Valor vacio
None # Siempre es con N mayuscula

contador = 0
while contador < 10:
    pass

nombres = ["juan", "pedro", "maria"]
for nombre in nombres:
    print(nombre)

"H" in "Hola"

for i in "hola":
    if "h" == i:
        print(True)


valor = 10
if valor == 5:
    print("Es 5")
elif valor == 15:
    print("Es 15")
elif valor == 20:
    print("Es 20")
else:
    print("No es 5, 15 ni 20")




if valor == 5:
    print("Es 5")
elif valor == 15:
    print("Es 15")
else:
    print("No es 5, 15 ni 20")


if valor == 5:
    print("Es 5")

# otra
if valor == 10:
    print("Es 10")
elif valor == 15:
    print("Es 15")

# Otra

if valor == 20:
    print("Es 20")

    while valor >= 20:
        print("Es 20")
        valor -= 1
else:
    print("No es 5, 15 ni 20")



# cuando usar : al final

# if
# elif 
# else


# while
# for

# with

# try
# except
# finally

# def
# class


"""
Palabaras reservadas
if
elif
else

def
class

try
except
finally

raise
with
import
from
as

# Solo dentro de funciones
break
continue
return

global
nonlocal
lambda

locals

assert

del
yield
pass
"""

# Mutabilidad de los tipos de datos
# mutables
conjuntos = {1,2,3}
listas = [1,2,3]
diccionarios = {1:2, 3:4}

lista = [1,2,3]
lista5 = lista
lista.append(4)

# No mutables
tupla = (1,2,3)
numero = 1233
flotante = 123.3
cadena = "Hola"
verdadero = True
falso = False
vacio = None


# Tipado dinamico
# Python es de tipado dinamico

valor = 10
id(valor)
valor = [1,5]
id(valor)

