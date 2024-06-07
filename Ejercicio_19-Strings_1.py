print('El trasistor puede ser de tipo "NPN" o "PNP"')  # Imprimir comillas dobles
print("El trasistor puede ser de tipo 'NPN' o 'PNP'")  # Imprimir comillas simples
print()
print('El trasistor puede ser de tipo "NPN" o "PNP"')  # Con el caracter scape \
print("El trasistor puede ser de tipo 'NPN' o 'PNP'")  # Con el caracter scape \
print()
print("Un semiconducor es de tipo \tNPN o PNP")  # Tabulador
print(
    'Un semiconducor es de tipo \t"NPN" o "PNP"'
)  # Tabulador y comillas dobles con scape \
print()
print("Un semiconducor es de tipo \nNPN o PNP")  # Salto de línea
print('Un semiconducor es de tipo \n"NPN" o "PNP"')  # Salto de línea y comillas
print()
print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)
print()
print(
    """Un transistor
pueder ser de tipo
\"NPN\" o \"PNP\" """
)  # Triple comilla para cadenas multilineas
print()
cadena = (
    'El trasistor puede ser de tipo "NPN" o "PNP"'  # Asignación de un string a variable
)
print(cadena)
cadena = 'El trasistor puede ser de tipo\n"NPN" o "PNP"'  # Varible con multilinea
print(cadena)
print()
cadena = 'El trasistor puede ser de tipo "NPN" o "PNP"'  # Suma de cadenas o strings
print(cadena + cadena)
print()
dos_cadenas = "El trasistor puede ser" 'de tipo: "NPN" o "PNP"'
print(dos_cadenas)
print()
cadena_2 = 'El trasistor puede ser de tipo "NPN" o "PNP"'
print("Contenido: " + cadena_2)
print()
cinco_espacios = " " * 5
print(cinco_espacios + "El trasistor puede ser" 'de tipo: "NPN" o "PNP"')
print()
# Buscar string
mensaje_1 = 'El trasistor puede ser de tipo "NPN" o "PNP"'

contador = mensaje_1.count('trasistor')
print(contador)
contador = mensaje_1.count('o')
print(contador)

print('Python' in mensaje_1)

print(mensaje_1.startswith('El'))

print(mensaje_1.endswith('PNP'))

print('tipo' in mensaje_1.lower())

print('transistor' not in mensaje_1.lower())