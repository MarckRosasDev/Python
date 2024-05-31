""" OPERADORES RELACIONALES
OPERADOR    DESCRIPCIÓN
>           Mayor que
<           Menor que
>=          Mayor o igual que
<=          Menor o igual que
==          Igual que
!=          Diferente que
"""

print(100 > 90)
print(100 < 90)
print(100 >= 90)
print(100 <= 90)
print(100 == 90)
print(100 != 90)

print("----Boleanos----")

print(True==True)
print(True==False)
print(True!=False)
print()
print(True>False)
print(True<False)
print(False>True)
print(False<True)

print("--------")

numero_uno = 78
numero_dos = 34

resultado = numero_uno < numero_dos
print(resultado)

resultado = numero_uno > numero_dos
print(resultado)

resultado = numero_uno <= numero_dos
print(resultado)

resultado = numero_uno >= numero_dos
print(resultado)

resultado = numero_uno == numero_dos
print(resultado)

resultado = numero_uno != numero_dos
print(resultado)

print("--------")

print(numero_uno == numero_dos * 3)
print((numero_uno**2 / 2) >= (numero_dos * 2 + 4))

print("----Strings----")

print("Python" == "Python")
print('Python' == 'Python')
print('Python' == "Python")
print()
print('Python'!='Python')
print()
palabra = 'Transistor'
print(palabra[0]=='T')
print('----Listas------')
lista_1=[1,2,3,4]
lista_2=[4,5,1,0]
print(lista_1==lista_2)
print(len(lista_1)==len(lista_2)) # Comparación de la longitud de las listas
print(lista_1[0]==lista_2[2])