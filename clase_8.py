# Los DOCString son cadenas de texto multilineas.
# Sirven para documentar nuestras clases y/o funciones.

# Type hints
# Sirven para documentar los valores que recibimos por parametro
# Sirve para documentar el tipo de dato de respuesta.
# los float son limitados.
# No se maneja plata con flotantes.
# Para eso usamos Decimal
# from decimal import Decimal


def suma(n1:int | float, n2: int | float) -> int | float:
    """Documentación
    Recibe 2 valores, n1 y n2. Retorna la suma de dichos valores."""
    return n1 + n2
print(suma(2,5))


def suma(n1:int | float, n2: int | float) -> tuple:
    return (n1, n2, n1 + n2)
print(suma(2,5))


def suma(n1:int | float, n2: int | float) -> list:
    return [n1, n2, n1 + n2]
print(suma(2,5))


def suma(n1:int | float, n2: int | float) -> dict:
    return {"n1": n1, "n2": n2, "resultado": n1 + n2}
print(suma(2,5))


def foo():
    return 2,3,4,5

a,b,c,d = foo()


def obtener_crea_usuario(email):
    """
    Devuelve (True, usuario) si el usuario se creo
    Devuelve (False, usuario) si el usuario ya existia.
    """
    # Obtener un usuario, si no existe, crealo
    # Acá hay una lógica blah
    usuario = {
        "nombre": "Juan",
        "email": "juan.bonini@bue.edu.ar"
    }
    return False, usuario

nuevo_usuario, usuario = obtener_crea_usuario("asd")

if nuevo_usuario:
    print(f"El usuario {usuario['email']} se creo correctamente")
else:
    print(f"El usuario {usuario['email']} ya existe en nuestro registro")

print(usuario)

# Flag = bandera
def operacion(n1, n2):
    resultado = n1 + n2
    flag_par = resultado % 2 == 0
    return flag_par, resultado


def operacion2(n1, n2):
    es_par = False
    resultado = n1 + n2
    
    if resultado % 2 == 0: # Chequeamos que un numero sea par o no
        es_par = True
        # La otra cosa a hacer
    return es_par, resultado

print(operacion(2,4))
print(operacion(2,5))


lista_numeros = [1,2,3]

for indice, numero in enumerate(lista_numeros):
    print(f"Indice: {indice}")
    print(f"Numero: {numero}")