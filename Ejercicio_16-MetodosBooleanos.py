cadena_texto = "El silicio es un semiconductor muy utilizado en la electrónica"
cadena_texto_2 = "EL SILICIO ES UN SEMICONDUCTOR MUY UTILIZADO EN LA ELECTRÓNICA"
cadena_texto_3 = "el silicio es un semiconductor muy utilizado en la electrónica"

print(cadena_texto.startswith("E"))  # True
print(cadena_texto.startswith("e"))  # False
print()
print(cadena_texto.endswith("A"))
print(cadena_texto.endswith("a"))
print()
print(cadena_texto.isupper())
print(cadena_texto_2.isupper())
print(cadena_texto_3.islower())
