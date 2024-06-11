# Realiza un programa el cual pida un número y te devuelva la tabla de multiplicar de ese número
print("--- Programa 1 ---")
numero = int(input("Ingresa el número del cual quieres saber su tabla: "))
multiplicacion = 0
i = 0
while i <= 10:
    multiplicacion = numero * i
    print(f"{numero} x {i} = {multiplicacion}")
    i += 1
print()

print("--- Programa 2 ---")
# Codifica un programa que pregunte tu edad y muestre los años que has cumplido desde el año 1 de edad
edad = int(input("Ingresa tu edad en años: "))
i = 1

while i <= edad:
    print(f"Has cumplido {i} años")
    i += 1
print()

print("--- Programa 3 ---")
# Crea un programa que ingrese una letra e indique si es vocal o no es vocal
letra = input('Ingresa una letra: ')
if letra.lower() in 'aeiou':
    print('La letra es una vocal')
else:
    print('La letra no es una vocal')
print()

print("--- Programa 4 ---")
num= int(input('Ingresa un número entero: '))
if num>0:
    print(f'El valor absoluto de {num} es: {num}')
else:
    print(f'El valor absoluto de {num} es: {abs(num)}')
print()

print("--- Programa 5 ---")
# Utilizando opradores lógicos, determina si una cadena de texto tiene una longitud mayor o igual a 5 y menor o igual a 10
cadena= input('Ingresa la cadena de texto: ')
if len(cadena)>=5 or len(cadena) <=10:
    print('La cadena es mayor que 5 caracteres pero menor que 10 caracteres.')
else:
    print('La cadena es menor de 5 caracteres o mayor de 10 caracteres.')