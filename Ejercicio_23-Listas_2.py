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

sum_lista=lista_1+lista_2 # Sumar dos listas
print(sum_lista)
print()
lista_edad=[]
while len(lista_edad)<5:
    edad= int(input('Ingresa la edad: '))
    lista_edad.append(edad) # Agregar un elemto a la lista
print(f'Las edades son: {lista_edad}')


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
lista_1.remove(
    "C#"
)  # Eliminar un elemento con remove (se debe de conocer el valor exacto del elemento)
print(lista_1)
del lista_1[0]  # Eliminar un elemento con del (por medio del índice)
print(lista_1)
del lista_1[1]
del lista_1[-1]
print(lista_1)
print()
lista_5 = [2, 6, 3, 1, 5, 6, 2, 3, 0, 4, 5]
lista_1.extend(lista_5)  # Agregar elementos de la lista 5 a la lista 1
print(lista_1)
print()

valor_seleccionado = lista_1[0]
print(valor_seleccionado)
# print(lista_1.count(1))
conteo_valor_seleccionado = lista_1.count(
    1
)  # Devuelve las veces que se repite un valor en la lista
print(
    f"El valor {valor_seleccionado} se repite {conteo_valor_seleccionado} veces en la lista 1"
)
print()

lista_6 = [5, 1, 2, 7, 23, 100, 4, 3, 4, 6, 1, 2, 3, 5]
print(lista_6.index(5))  # Busca el PRIMER valor que está en la lista
print(lista_6)
lista_6.sort()
print(lista_6)
lista_6.reverse()
print(lista_6)
print()

lista_7 = ['Capacitor', 3.1416, 500,'Optoacoplador', 'Resistencia', 'Inductor']
print(lista_7)
lista_7[2]='Transistor' # Cambiar el valor de un dato por el índice
print(lista_7)
lista_7.pop() # Elimina el último elemento de la lista
print(lista_7)
lista_7.remove(3.1416)
lista_7.remove('Capacitor')
print(lista_7)