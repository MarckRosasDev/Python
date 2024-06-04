"""Se pueden solucionar empleando las reglas de precedencia:

Primero los paréntesis que indican prioridad.
Segundo, las expresiones aritméticas por sus propias reglas.
Tercero, las expresiones relacionales.
Cuarto, las expresiones lógicas.
"""

a = 20
b = 10

print(a * b - 2**b >= 20 and not (a % b) != 0)