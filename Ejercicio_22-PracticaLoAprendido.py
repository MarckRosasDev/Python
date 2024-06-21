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
letra = input("Ingresa una letra: ")
if letra.lower() in "aeiou":
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")
print()

print("--- Programa 4 ---")
num = int(input("Ingresa un número entero: "))
if num > 0:
    print(f"El valor absoluto de {num} es: {num}")
else:
    print(f"El valor absoluto de {num} es: {abs(num)}")
print()

print("--- Programa 5 ---")
# Utilizando opradores lógicos, determina si una cadena de texto tiene una longitud mayor o igual a 5 y menor o igual a 10
cadena = input("Ingresa la cadena de texto: ")
if len(cadena) >= 5 or len(cadena) <= 10:
    print("La cadena es mayor que 5 caracteres pero menor que 10 caracteres.")
else:
    print("La cadena es menor de 5 caracteres o mayor de 10 caracteres.")
print()

print("--- Programa 6 ---")
# Codifica un programa que solicite 2 palabras y ue indique si riman.
# Condiciones: Si las 3 últimas letras coinciden se despliega: Riman.
#  Si las 2 últimas letras coinciden se despliega: Riman un poco.
#  Si no coinciden las últimas letras se despliega: No riman.
palabra_1 = input("Ingresa la primera palabara: ")
palabra_2 = input("Ingresa la segunda palabara: ")

if len(palabra_1) < 3 or len(palabra_2) < 3:
    print("Las palabras tienen menos de 3 caracteres, por lo tanto, no riman.")
elif palabra_1[-3:] == palabra_2[-3:]:
    print("Riman.")
elif palabra_1[-2:] == palabra_2[-2:]:
    print("Riman un poco.")
else:
    print("No riman.")

print("--- Programa 7 ---")
# Es necesario crear un programa que permita obtener la calificación total de un curso.
# La calificación final se compone de los siguiente:
# Proyecto final: 50%    Expocisiones: 25%    Tareas: 15%  Asistencia: 10%
# Las calificaciones obtenidas por el alumno son:
# Proyecto final: 6.5    Expocisiones: 8      Tareas: 7    Asistencia: 9
# Extra: Ingresa las calificaciones por medio de la función input. 

porcentaje_proyecto_final = 50 / 100
porcentaje_exposiciones = 25 / 100
porcentaje_tareas = 15 / 100
porcentaje_asistencia = 10 / 100

"""
calificacion_proyecto_final = 6.5
calificacion_exposiciones = 8
calificacion_tareas = 7
calificacion_asistencia = 9
"""
calificacion_proyecto_final = float(input('Ingresa la calificación del proyecto final: '))
calificacion_exposiciones = float(input('Ingresa la calificación de las exposiciones: '))
calificacion_tareas = float(input('Ingresa la calificación de las tareas: '))
calificacion_asistencia = float(input('Ingresa la calificación de la asistencia: '))



ponderacion_proyecto_final = calificacion_proyecto_final * porcentaje_proyecto_final
ponderacion_exposiciones = calificacion_exposiciones * porcentaje_exposiciones
ponderacion_tareas = calificacion_tareas * porcentaje_tareas
ponderacion_asistencia = calificacion_asistencia * porcentaje_asistencia

calificacion_final=ponderacion_proyecto_final+ponderacion_exposiciones+ponderacion_tareas+ponderacion_asistencia
print(f'La calificación del alumno es: {calificacion_final}')
print()

print("--- Programa 8 ---")
# Realiza un programa que sume todos los números enteros pares dele el número cero
# hasta un número ingresado por el usuario por medio del teclado.

limite = int(input('Ingresa el límite: '))
suma = 0
for numero in range(0, limite+1,2):
    if numero % 2 ==0:
        suma += numero

print(f'La suma de los pares desde el 0 hasta {limite} es: {suma}') 