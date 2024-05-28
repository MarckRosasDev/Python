"""
REGLA PEMDAS:

Paréntesis
Exponentes
Multiplicación y División (de izquierda a derecha)
Adición y Sustracción (de izquierda a derecha)
"""

num_1 = 20
num_2 = 15
num_3 = 50
num_4 = 10

print(num_1 + num_2)
print((num_1 + num_2) * num_3)
print((num_1 + num_2) * num_3-num_4)
print((num_1 + num_2) * (num_3-num_4))
print((num_1 + num_2) * (num_3-num_4)/(num_1-num_2))

print('---------------')
resultado = (2+3)*4/(5-1)
print('El resultado es: '+str(resultado))
"""
En este ejemplo, las operaciones se realizarán en el siguiente orden:

1) (2 + 3): Se calcula la suma dentro de los paréntesis, dando como resultado 5.
2) 5 * 4: Se realiza la multiplicación, obteniendo como resultado 20.
3) 5 - 1: Se efectúa la resta, obteniendo como resultado 4.
4) 20 / 4: Finalmente, se realiza la división, dando como resultado 5.
"""
