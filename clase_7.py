# Funciones

# Definimos la función sin parametros
def foo():
    return "Hola mundo"

print(foo())

def suma(a, b):
    # El return sale de la función.
    return a + b # El return devuelve el valor

def suma2(a, b):
    resultado = a + b
    # Manipulamos el resultado
    return resultado # Devolvemos el resultado


print(suma(10, 10))

# La idea siempre es almacenar resultado de una función
# para poder seguir trabajando
resultado = suma(2, 2)
print(f"El resultado de la suma es: {resultado}")

print() # Invocamos, llamamos.

# x + y = z

def foo(a):
    # Bloque if / elif
    if a == 5:
        return "El valor es 5"
    elif a == 9:
        return "El valor es 9"

    return "El valor no es ni 5 ni 9"

print(foo(9))



def suma_enteros_positivos(n1: int, n2: int) -> int | None:
    if n1 >= 0 and n2 >= 0:
        if type(n1) is int and type(n2) is int:
            return n1 + n2

res1 = suma_enteros_positivos(1, 6)
print(f"El resultado de suma_enteros_positivos es: {res1}")

res2 = suma_enteros_positivos(1.0, 6)
print(f"El resultado de suma_enteros_positivos es: {res2}")

def suma_enteros_positivos2(n1: int, n2: int) -> int | None:
    resultado = None
    if n1 >= 0 and n2 >= 0:
        if type(n1) is int and type(n2) is int:
            resultado = n1 + n2
    return resultado


res3 = suma_enteros_positivos2(1, 6)
print(f"El resultado de suma_enteros_positivos es: {res3}")
res4 = suma_enteros_positivos2(1.0, 6)
print(f"El resultado de suma_enteros_positivos es: {res4}")

def foo2(a, b):
    resultado = a + b # Devuelve None

print(foo2(5, 9))


if type(10) is int:
    pass


while True:
    n1 = int(input("Ingresar primer numero: "))
    n2 = int(input("Ingresar segundo numero: "))

    print(suma(n1, n2))
