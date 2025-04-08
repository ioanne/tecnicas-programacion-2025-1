# Hola

# Variables
# Semantico
nombre = "Juan"
apellido = "Bonini"

# Error sintaxis
edad: 50 # Manera incorrecta de definir una variable.

a = 20
b = 5

r_s_e = 4 + 5

# Esto es mejor
resultado_suma_entero = 4 + 5


# Tipos de datos simples
# Cadena de texto (str)
# Numeros enteros (int)
# Numeros flotantes (float)
# Sin valor (None) # Equivalente a null
# Verdaderos o falso (boolean)


# Tipos de datos más complejos
# multiples valores mutables (list)
# multiples valores no mutables (tuple)
# Valores con nombre llamado diccionario (dict)
# Conjunto de datos (set)


# Listas
# Almacenan valores de cualquier tipo
lista_valores = ["Hola", 1, 2.0, True, None]

# Una lista puede contener cualquier otra cosa
# Puede ser una lista que contiene listas que contiene listas
lista_valores_2 = [
    ["Hola", 1, 2.0, 20, 25, None],
    ["Chau!", 1, 2, ["Hola de nuevo!"]]
]

lista_valores_2[0]
lista_valores_2[1][-1]


# Todo contenido en una lista
ejemplo_lista = [
    [
        'cadena texto',
        1, 
        [1, 2, 3]
    ],
    [
        1,
        2,
        3,
        ['texto']
    ],
    [
        1,
        2,
        [1,2,3,4,5,6,7,8,9]
    ]
]

print(ejemplo_lista[0][0]) # cadena texto
print(ejemplo_lista[0][1]) # 1
print(ejemplo_lista[1][0]) # 1
print(ejemplo_lista[1][3][0]) # texto
print(ejemplo_lista[2][2][0]) # 1
print(ejemplo_lista[2][2][6]) # Debe devolver 7
print(ejemplo_lista[2][2][-3]) # Debería devolver 7


# Diccionario
# Tipos de datos clave/valor

dict2 = {1:1, 2:2, 3:"", 4:{1:256}}
dict3 = {"numero_1":1, "numero_2":2, "numero_3":"", "numero_4":{"clave_6":256}}

"""
    Claves para diccionarios.

    Se recomienda que no tengan espacios
    se puede separar por _
    ejemplo: empleado_1

    La clave puede ser cualquier cosa no mutable.
"""
print(dict3["numero_4"]["clave_6"])
print(dict2[1])
print(dict3["numero_1"])

print(dict2[4][1])


"""
    Definir la estructura de un diccionario
    Las claves que van a componer nuestro diccionario
    nombre, apellido, edad, domicilio

"""

personas = {
    "empleado_1": {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 20,
        "domicilio": "Avenida siempre viva 456"
    },
    "empleado_2": {
        "nombre": "Maria",
        "apellido": "Fernandez",
        "edad": 40,
        "domicilio": "Juramento 4000"
    },
    "empleado_3": {
        "nombre": "Jose",
        "apellido": "Martinez",
        "edad": 33,
        "domicilio": "Juramento 3456"
    },
}

# Algoritmo 1   itera 3 veces
    # Clave         # Valor
for identificacion, persona in personas.items():
    print(f"La identificacion del usuario es: {identificacion}")
    print(f"El nombre es {persona['nombre']}")
    print(f"El apellido es {persona['apellido']}")
    print(f"La edad es {persona['edad']}")
    print(f"El domicilio es {persona['domicilio']}")


# Algoritmo 2   (3x4) 12 iteraciones
for k, v in personas.items():
    print(f"El usuario con id {k}:")
    for clave, valor in v.items():
        print(f"El {clave} es {valor}.")

# Bucle for
# Los bucles funcionan con cualquier tipo de datos iterable
lista = [1,2,3,4,5]

# El bucle comienza con la palabra reservada for
# Luego viene una variable que se esta definiendo de forma temporal
# la palabra reservada in es para indicar que es lo que se recorre

for variable in lista:
    print(variable)


# Recorrer un string
for letra in "Hola":
    print(letra)


# Variable sin declarar
print(letra)
# Acá no esta mas la variable letra.


cadena = "Esto es una cadena de texto"
for letra2 in cadena:
    if letra2 == "c":
        continue
    print(letra2, end="")

cadena = "Esto es una cadena de texto"
for letra2 in cadena:
    if letra2 == "c":
        break
    print(letra2, end="")


# Break y continue
# break lo que hace es forzar la salida de un bucle
# continue lo que hace es forzar continuar con el proximo elemento

print()
while True:
    # Bucle infinito
    # Todo bucle "inifinito" se tiene que poder controlar
    valor = input("Ingrese valor: ")
    if valor == "salir":
        break
    # Ejecutar algoritmo!
    print(valor)


valor = input("Ingrese valor: ")
print(valor)