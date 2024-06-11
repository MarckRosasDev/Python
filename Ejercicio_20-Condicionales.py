print("--- if ---")
if True:
    print("Entraste a la condición if - True")

if False:
    print("Entraste a la condición if - False")
print()

# Encadenación de if
numero = 10
if numero == 5:
    print("Numero equivale a 5")
if numero == 10:
    print("Número equivale a 10")
print()

# Anicación de if
numero_1 = 20
numero_2 = 30

if numero_1 == 20:
    print(f"Numero_1 equivale a {numero_1}")
    if numero_2 == 30:
        print(f"Numero_2 equivale a {numero_2}")
print()

# Evaluación de múltiples expresiones
if numero_1 == 20 and numero_2 == 30:
    print(f"Numero_1 equivale a 20 y Numero_2 equivale a 30")

if 1 < 20 or 2 > 30:
    print("1 es menor que 20")
    if 2 > 30:  # False
        print("2 es mayor que 30")
print()
print("--- else ---")
numero = 33
if numero % 2 == 0:
    print(f"{numero} es un número par")
else:
    print(f"{numero} es un número impar")
print()
print('--- elif ---')
calificacion = float(input('Introduce tu calificación: '))
if calificacion == 10:
    print('Tu calificación es sobresaliente')
elif calificacion == 9:
    print('Tu calificación es notable')
elif calificacion == 8:
    print('Tu calificación es buena')
elif calificacion == 7:
    print('Tu calificación es suficiente')
elif calificacion <=6:
    print('Tu calificación es insuficiente, no aprobaste')
else:
    print('Calificación fuera de rango')