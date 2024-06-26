# Es un tipo de colección de datos ordenada. Equivale a arrays o vectores en otros lenguajes.
# Se recomienda que sean de un solo tipo de dato.
# Los datos pueden mutar, se puede agregar, eliminar o modificar elementos.
# Sintaxis: Se crean utilizando corchetes []. Los elementos se separan por comas, y las listas vacías se definen como [].
# Uso: Si necesita crear una lista dinámica de elementos que se pueden cambiar o reordenar, use una lista.

lista = ["Hola", "mundo", "Python"]
print(lista)
print(type(lista))
print(lista[0])
print(type(lista[0]))
print()
lista_numeros = [1, 2, 3, 4, 5]
print(lista_numeros)
print(type(lista_numeros))
print(lista_numeros[0])
print(type(lista_numeros[0]))
print()
lista_flotantes = [1, 44.44, 3.1416, -1.6, 33.33]
print(lista_flotantes)
print(type(lista_flotantes))
print(lista_flotantes[3])
print(type(lista_flotantes[3]))
print(len(lista_flotantes))
print()
print("--- Slicing ---")
datos = [3.1416, "Python", -3.333, 800, "C#"]
#       0           1       2     3     4
print(len(datos))
print(datos[0])
print()
print("datos[0:0]")
print(datos[0:0])
print(datos[1:0])
print(datos[2:0])
print(datos[3:0])
print(datos[4:0])
print()
print("datos[0:1]")
# print(datos[0:0])
print(datos[0:1])
print(datos[0:2])
print(datos[0:3])
print(datos[0:4])
print(datos[0:5])
print()
print("datos[0:]")
# print(datos[:])
print(datos[0:])
print(datos[1:])
print(datos[2:])
print(datos[3:])
print(datos[4:])
print()
print("datos[:0]")
# print(datos[:])
print(datos[:0])
print(datos[:1])
print(datos[:2])
print(datos[:3])
print(datos[:4])
print(datos[:5])
print()
print(datos[-1])
print(datos[-5:-1])
print()
# Actualización de los datos de la lista
letras = ["a", "b", "c", "d", "e", "f", "g"]
print(letras)
letras[:3]=['A','B','C']
print(letras)
print()
print("--- Mutabilidad ---")
print(datos)
datos[0] = "TRIAC"
print(datos)