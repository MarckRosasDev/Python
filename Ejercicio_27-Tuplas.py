# Colecciones ordenadas e inmutables de elementos de cualquier tipo.
# Se utilizan para almacenar datos que no se van a modificar.
tupla = ("Python", 3.1416, "Silicio", -88.9)
print(tupla)
print(type(tupla))
print()
print(tupla[0])
print(tupla[-1])
print(tupla[1:])
print(tupla[:2])
print()
# tupla[0] = 100 # Es inmutable
print(tupla.index("Silicio"))  # Busca un elemento y devuelve su posición en la tupla
# print(tupla.index('silicio'))
print()
print(tupla.count("Python"))  # Cuenta cuantas veces aparece un elemento en la tupla
print(tupla.count("Electrón"))
print()
# tupla.append(22.89) # Las tuplas son inmutables,no es posible modificar su contenido
