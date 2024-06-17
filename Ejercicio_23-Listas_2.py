print("--- Listas anidadas ---")
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]
lista_3 = [11, 12, 13, 14, 15]
lista_4 = [16, 17, 18, 19, 20]
anidadas = [lista_1, lista_2, lista_3, lista_4]
print(anidadas)
print(anidadas[0])  # lista 1
print(anidadas[-1])  # última lista
print()
print(anidadas[0][0])  # Primer sublista, primer ítem de la misma
print(anidadas[3][2])  # cuarta sublista, segundo ítem de la misma
print()
print("--- Métodos ---")
print(lista_1)
lista_1.append(10)  # Agregar elementos
print(lista_1)
lista_1.append("C#")
print(lista_1)
lista_1.insert(1, 19.78)
print(lista_1)
lista_1.insert(0, "Capacitor")
print(lista_1)
lista_1.remove("C#")  # Eliminar un elemento con remove (se debe de conocer el valor exacto del elemento)
print(lista_1)
del lista_1[0]  # Eliminar un elemento con del (por medio del índice)
print(lista_1)
del lista_1[1]
del lista_1[-1]
print(lista_1)
print()
lista_5= [2,6,3,1,5,6,2,3,0,4,5]
lista_1.extend(lista_5) # Agregar elementos de la lista 5 a la lista 1
print(lista_1)
print()

valor_seleccionado=lista_1[0]
print(valor_seleccionado)
#print(lista_1.count(1))
conteo_valor_seleccionado = lista_1.count(1) # Devuelve las veces que se repite un valor en la lista
print(f'El valor {valor_seleccionado} se repite {conteo_valor_seleccionado} veces en la lista 1')