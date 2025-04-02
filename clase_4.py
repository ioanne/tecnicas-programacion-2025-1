
"""
Una funcion se DEFine usando la palabra reservada def.
def [nombre_funcion]():
   variable = 10
   resultado = variable * 2
   return resultado
"""
def foo():
    return 2

r = foo()
resultado = r + 4
print(resultado)


def suma(a, b):
    return a + b

resultado = suma(a=2, b=5)
print(resultado)