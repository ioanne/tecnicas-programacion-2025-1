
# Bucle for
for letra in "Python":
    print("Letra:", letra)

lista = [1,2,3,4]
for valor in lista:
    # lista.append(1) # Esta linea hace que se convierta en un bucle infinito
    print(valor)

# Duplicar el valor al final de la lista
# Bucle while
lista = [11,22,33,44,55] # 11,22,33,44,55,22,44,66....
contador = 0
cantidad_maxima = 5
while contador < cantidad_maxima:
    resultado = lista[contador] * 2
    lista.append(resultado)
    print("Recorriendo el elemento en la posición", contador, "valor: ", lista[contador])
    contador += 1
print(lista)

for numero in range(0, 100): # desde un valor hasta el valor que no queremos
    print(numero)
