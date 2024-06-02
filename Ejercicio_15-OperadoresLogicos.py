# OPERADORES LÓGICOS
"""
1) not: Niega el valor booleano de su operando. Es decir, si el operando es True, el resultado será
False, y si el operando es False, el resultado será True.
2) and: Evalúa si ambos operandos son True. Si ambos operandos son True, el resultado será True; en
caso contrario, el resultado será False.
3) or: Evalúa si al menos uno de los operandos es True. Si uno o ambos operandos son True, el 
resultado será True; en caso contrario, el resultado será False.
"""
print("---not---")
print(not True)
print(not False)

print(not False == True)
print()
print(not 1)
print(not 0)
print()

print("---and---")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()
print(1 and 1)
print(1 and 0)
print(0 and 1)
print(0 and 0)

print("---or---")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()
print(1 or 1)
print(1 or 0)
print(0 or 1)
print(0 or 0)
print("-------")
print(5 > 0 and 3 < 8)
print(5 > 0 and 3 < 8 or 0 > 1)
print(5 > 0 and 3 < 8 or 0 > 1 and not 1)
print()
a = 35
b = 60
print(a < b and b < a)
print(a < b or b < a)
print('---String---')
cadena = 'Hola Python'
print(len(cadena)==10)
print(cadena[0]=='H')
print(len(cadena)==10 or cadena[0]=='H')