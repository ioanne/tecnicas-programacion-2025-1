# 
variable = 10
variable2 = "Hola"
variable3 = 1.4
lista = [1,2,3]
diccionario = {"Hola": "Chau"}

mix_personas = [
    {"identificador": 1, "nombre": "Pedro"},
    {"identificador": 2, "nombre": "Jose"},
    {"identificador": 3, "nombre": "Juan"},
]

def identificar_persona(mix_personas: list, nombre: str) -> dict | None:
    for persona in mix_personas:
        if persona["nombre"] == nombre:
            return persona

persona = identificar_persona(mix_personas, "Pedro")
print(f"Identificando a la persona: {persona}")

print(id(identificar_persona))

# Almaceno la función en "funcionalidad"
funcionalidad = identificar_persona

resultado = funcionalidad(mix_personas, "Pedro")
print(f"Guardamos la funcion en otra variable y la ejecutamos: {resultado}")

print(id(funcionalidad))


mostrar_mensaje_en_pantalla = print

mostrar_mensaje_en_pantalla("Mostrando mensaje")


def suma(a: int, b: int) -> int:
    return a + b

def resta(a: int, b: int) -> int:
    return a - b

def multiplicación(a: int, b: int) -> int:
    return a * b



def resolver_operación(operación_1, operación_2, valor1, valor2) -> int:
    resultado_1 = operación_1(valor1, valor2)
    resultado_2 = operación_2(valor1, valor2)
    return resultado_1, resultado_2

print(resolver_operación(suma, resta, 10, 5))


operaciones = [
    {
        "función": resta,
        "valores": [5, 4]
    }, {
        "función": suma,
        "valores": [6, 2]
    },
    {
        "función": multiplicación,
        "valores": [3, 2]
    }
]



def resolver_operaciones(operaciones: list) -> list:
    resultados = []
    for operación in operaciones:
        resultado = operación["función"](operación["valores"][0], operación["valores"][1])
        resultados.append(resultado)
    return resultados


print(f"Resultados: {resolver_operaciones(operaciones)}")



diccionario = {
    "función": suma,
    "valores": [1, 2]
}

lista = [suma]


funcion = suma

print(funcion)
print(suma)
print(diccionario["función"])
print(lista[0])


tupla_inteligente = (suma, 1, 5)

resultado2 = tupla_inteligente[0](tupla_inteligente[1], tupla_inteligente[2])
print(resultado2)

print(suma(1, 5))


class Operacion:
    def __init__(self):
        print(id(self))

    def suma(self, a: int, b: int) -> int:
        return a + b
    
    def resta(self, a: int, b: int) -> int:
        return a - b
    
    def multiplicación(self, a: int, b: int) -> int:
        return a * b
    
    def división(self, a: int, b: int) -> int:
        return a / b


def resta(a: int, b: int) -> int:
    return a - b


_operacion = Operacion() # instanciar una clase
_operacion.suma = resta

print(_operacion.suma(10, 5))

