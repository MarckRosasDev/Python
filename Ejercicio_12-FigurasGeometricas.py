#Calcula el área de un círculo

import math

print('ÁREA DE UN CÍRCULO')
radio = float(input("Ingrese el radio del círculo: "))
area_circulo = math.pi * radio ** 2
print(f"El área del círculo es: {area_circulo:.2f} unidades cuadradas")
"""
{area}: Esta es una expresión que se inserta dentro de la cadena de texto.
Se refiere a la variable area, que presumiblemente contiene el valor del área del círculo.

:.2f: Este es un formateador de número que indica que el valor de la variable area debe
imprimirse como un número decimal con dos dígitos después del punto decimal.
"""
print('---------')

#Calcula el área de un cuadrado
print('ÁREA DE UN CUADRADO')
lado = float(input("Ingrese la longitud de un lado del cuadrado: "))
#area_cuadrado = lado ** 2
area_cuadrado = pow(lado,2)
print(f"El área del cuadrado es: {area_cuadrado:.2f} unidades cuadradas")
print('---------')

#Calcula el área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2
print(f"El área del triángulo es: {area_triangulo:.2f} unidades cuadradas")
