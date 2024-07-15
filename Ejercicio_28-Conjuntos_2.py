# Operaciones con conjuntos

conjunto_a = {"Chilaquiles", "Estrujadas", "Arroz con plátano", "Mole de Xico", 'Zacahuilt'}
conjunto_b = {"Zacahuilt", "Picadas", "Panuchos", "Mole de Xico", "Tamales aguados"}
print(conjunto_a)
print(conjunto_b)
print()

print("--- Unión ---")

conjunto_union = conjunto_a.union(conjunto_b)
print(conjunto_union)
print(conjunto_a | conjunto_b)
print()

print("--- Intersección ---")

conjunto_interseccion = conjunto_a.intersection(conjunto_b)
print(conjunto_interseccion)
print(conjunto_a & conjunto_b)
print()

print("--- Diferencia ---")

conjunto_diferencia=conjunto_a.difference(conjunto_b)
print(conjunto_diferencia)
print(conjunto_a-conjunto_b)
print()

print("--- Diferencia simétrica ---")

conjunto_diferencia_simetrica=conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_diferencia_simetrica)
print(conjunto_a ^ conjunto_b )