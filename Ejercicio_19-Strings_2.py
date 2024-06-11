palabra = "Electronica"
print(palabra[0])
print(palabra[1])
print(palabra[2])
print()
print(palabra[-1])  # Última posición de la cadena de caracteres
print(palabra[-2])
print(palabra[-3])
print()
print("--- Slicing ---")
print(palabra[0:5])  # [Inicio:Fin]
print(palabra[0:])  # [0: Fin]
print(palabra[2:])
print(palabra[-2:])
print(palabra[:2])  # [Inicio:2]
print(palabra[:-2])
print(palabra[:])
print(palabra[:2] + palabra[2:])
print()
# print(palabra[58]) -> Error
print("--- Inmutabilidad ---")
# palabra[0]=H -> Error
# NO se puede modificar el contenido de una cadena
# Sí se puede concatenar y/o utilizar slicing con otras cadenas o caracter
palabra = "e" + palabra[1:]
print(palabra)
print()
print("--- Longitud ---")
palabra = "Electrón"
print(len(palabra))