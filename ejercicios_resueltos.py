"""
Ejercicio 5: Competencia de reciclaje entre barrios
Una competencia de reciclaje se llevó a cabo entre varios barrios, y estos son los resultados:


resultados = [
    {"barrio": "Villa Urquiza", "kilos_reciclados": 25},
    {"barrio": "Belgrano", "kilos_reciclados": 30},
    {"barrio": "Recoleta", "kilos_reciclados": 22},
    {"barrio": "Flores", "kilos_reciclados": 27}
]
Objetivo:
● Mostrá qué barrio recicló más kilos (el que tenga más kilos_reciclados).
● Mostrá todos los barrios con la cantidad que reciclaron.

Pista:
Recorré la lista con un for, y usá una variable para ir guardando el barrio que más recicló.
"""

resultados = [
    {"barrio": "Villa Urquiza", "kilos_reciclados": 25}, # Diccionario
    {"barrio": "Belgrano", "kilos_reciclados": 30}, # Diccionario
    {"barrio": "Recoleta", "kilos_reciclados": 22}, # Diccionario
    {"barrio": "Flores", "kilos_reciclados": 27} # Diccionario
]

# Paso 1
# ● Mostrá qué barrio recicló más kilos (el que tenga más kilos_reciclados).

# Algoritmo de máximo lineal
barrio_ganador = ''
cantidad_kilos_ganador = 0

for resultado in resultados:
    barrio = resultado['barrio'] # Obtenemos el barrio
    kilos_reciclados = resultado['kilos_reciclados'] # Obtenemos los kilos reciclados

    if kilos_reciclados > cantidad_kilos_ganador:
        cantidad_kilos_ganador = kilos_reciclados
        barrio_ganador = barrio


print(f"El barrio ganador es: {barrio_ganador} con {cantidad_kilos_ganador}")
print("=" * 120)

# Mostrá todos los barrios con la cantidad que reciclaron.
for resultado in resultados:
    barrio = resultado['barrio']

    if barrio == barrio_ganador: # Si es igual al barrio que no queremos
        continue

    kilos_reciclados = resultado['kilos_reciclados'] # Obtenemos los kilos reciclados
    print(f"Barrio: {barrio}")
    print(f"Kilos reciclados: {kilos_reciclados}")




resultados_reciclado = [
    {"barrio": "Villa Urquiza", "kilos_reciclados": 25}, # Diccionario
    {"barrio": "Belgrano", "kilos_reciclados": 30}, # Diccionario
    {"barrio": "Recoleta", "kilos_reciclados": 22}, # Diccionario
    {"barrio": "Flores", "kilos_reciclados": 27} # Diccionario
]



resultados_tenis = [
    {"barrio": "Villa Urquiza", "puntaje": 25}, # Diccionario
    {"barrio": "Belgrano", "puntaje": 30}, # Diccionario
    {"barrio": "Recoleta", "puntaje": 22}, # Diccionario
    {"barrio": "Flores", "puntaje": 27} # Diccionario
]


resultados_mundial = [
    {"pais": "Argentina", "puntaje": 110}, # Diccionario
    {"pais": "Chile", "puntaje": 60}, # Diccionario
    {"pais": "Holanda", "puntaje": 90}, # Diccionario
    {"pais": "Francia", "puntaje": 109} # Diccionario
]


# Implementar funcion
# Manera con un solo for
def obtener_mayor(resultados: list, clave: str) -> dict:
    valor_maximo = 0
    for resultado in resultados:
        valor = resultado[clave]
        if valor > valor_maximo:
            valor_maximo = valor
            ganador = resultado
    return ganador

ganador = obtener_mayor(resultados, 'kilos_reciclados')

print("=" * 120)
print(f"El barrio ganador es: {ganador['barrio']} con {ganador['kilos_reciclados']}")

ganador = obtener_mayor(resultados_tenis, 'puntaje')

print("=" * 120)
print(f"El barrio ganador es: {ganador['barrio']} con {ganador['puntaje']}")

ganador = obtener_mayor(resultados_mundial, 'puntaje')

print("=" * 120)
print(f"El pais ganador es: {ganador['pais']} con {ganador['puntaje']}")