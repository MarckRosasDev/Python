miVariable1 = 'Python'
print(miVariable1)
print(type(miVariable1)) # string

print('----------------')

miVariable2= '2024'
print(miVariable2)
print(type(miVariable2)) # string

print('----------------')

miVariable3= 2024
print(miVariable3)
print(type(miVariable3)) # int

print('----------------')

miVariable4= 3.333
print(miVariable4)
print(type(miVariable4)) # float

print('----------------')

miVariable5= True
print(miVariable5)
print(type(miVariable5)) # boolean

print('----------------')

miVariable6= "Transistor" # Comillas dobles
print(miVariable6)
print(type(miVariable6)) # string

print('----------------')

# Suma y concatenación de variables
print(miVariable1+miVariable2) # Cadenas de texto (string)
print(miVariable3+miVariable4) # Entero y flotante
# print(miVariable1+miVariable3) #Indica error al no ser tipos compatibles 

print('----------------')

nombre= 'Marco'
print('Hola '+ nombre+'.')

print('----------------')

nombres, apellido, titulo = 'Marco A', 'Olmos', 'Ing.'
mensaje = 'Python'
print(f'Hola, {titulo} {nombres}. Estás apendiendo {mensaje} en 2024')

print('----------------')

nombre_completo = 'Mr. ' + nombre + ' '+apellido + '.'
print(nombre_completo)

nombre_completo = 'Mr. %s %s.' %(nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'O')
print(nombre_completo)

nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'O')
print(nombre_completo)

nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido='R'
)

print('----------------')

# TIPADO

variable='Marco'
print(variable)
print(type(variable))

variable=2024
print(variable)
print(type(variable))

variable=38.97
print(variable)
print(type(variable))

variable= False
print(variable)
print(type(variable))

variable='A'
print(variable)
print(type(variable))

print('----------------')
# Constantes
ESTO_ES_UNA_CONSTANTE = 3.1416
print(ESTO_ES_UNA_CONSTANTE)

