# Recorrimos una lista usando While
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(lista_numeros):
    print(lista_numeros[i])
    i += 1
print()
# Recorrimos una lista usando for
for numero in lista_numeros:
    print(numero)
print()
# Modificación de los valores de la lista
indice = 0
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    numeros[indice] *= 2
    indice += 1
print(numeros)
print()
# Modificación de los valores de la lista con la función enumerate
#print(indice)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 100
print(numeros)
print()
# for para cadenas
mensaje = 'Estoy aprendiendo Python'
for caracter in mensaje:
    print(caracter)
print()
# función range
for i in range(25):
    print(i)