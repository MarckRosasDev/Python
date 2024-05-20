print('Este es un mensaje')

print('Este es un segundo mensaje.', end='')
print('Este es un tercer mensaje.', end='')

print()

print('Este', 'es', 'un', 'cuarto', 'mensaje', sep='-')

print('Hola', 'mundo', 1.6, (1,2,3))

print('{} poco a poco {}'.format('Aprendiendo', 'Python'))

# Caracteres especiales \t  \n

print('Este es un texto\tcon una tabulación')
print('Este es un texto\ncon un salto de línea')
print(r"C:\user\directorio") # r(cadena) ->raw(cruda)
print("""Primera línea
      segunda línea
      tercera línea""")

cadena='Primera línea\nSegunda línea'
print(cadena)
print(cadena+cadena)

cadenas = 'Primera cadena' 'Segunda cadena'
print(cadenas)

cinco_espacios = ' '*5
print(cinco_espacios+'Este texto tiene 5 espacios')