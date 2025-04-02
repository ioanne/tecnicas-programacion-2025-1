# temperatura = 32
# if temperatura > 30:
#     print("Hace mucho calor, lleva agua.")
# elif temperatura >= 20:
#     print("El clima está agradable.")
# else:
#     print("Hace frío, lleva abrigo.")

"""
Instrucciones
1. Pide al usuario su edad.
2. Si tiene 18 años o más, imprime Eres mayor de edad.
3. Si no, imprime Eres menor de edad.
"""

# la función int nos permite convertir una cadena de texto en un entero.
# Siempre y cuando la cadena de texto contenga un numero entero.
edad_ingresada = input("Ingresar edad: ")
edad = int(edad_ingresada)

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
