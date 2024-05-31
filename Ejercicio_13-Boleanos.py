print(1 + 1 == 2)  # True
print(1 + 1 == 3)  # False

verdadero = True
# True (Verdadero): Representa una condición positiva o afirmativa.
falso = False
# False (Falso): Representa una condición negativa o no afirmativa.

print(type(verdadero))
print(type(falso))

print('Representación aritmética de True y False equivale a 1 y 0 respectivamente')
print(True*10)
print(True/10)
print(True-10)
print(True+10)
print()
print(False*10)
print(False/10)
print(False-10)
print(False+10)
print()
print(True+False)
print(True-False)
print(True*False)
#print(True/False)
print(False/True)

"""
Representación: Los valores booleanos se representan como True o False en el código.

Operadores: Se pueden utilizar operadores lógicos como and, or, not para combinar valores booleanos y realizar comparaciones.

Expresiones lógicas: Las expresiones lógicas son combinaciones de operadores booleanos y valores booleanos que se evalúan como True o False.

Condiciones: Las condiciones en Python utilizan expresiones lógicas para determinar qué código se debe ejecutar. Por ejemplo, un bloque if se ejecuta solo si la condición especificada es True.
"""
"""
Conversión de tipos:

Es posible convertir otros tipos de datos a booleanos en Python. Algunos ejemplos:

Números: Un número distinto de 0 se convierte en True, mientras que 0 se convierte en False.

Cadenas: Una cadena vacía ("") se convierte en False, mientras que cualquier cadena con contenido se convierte en True.

Objetos: Los objetos en Python se evalúan como True a menos que tengan un método especial __bool__ que devuelva False.
"""
