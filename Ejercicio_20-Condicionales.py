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

print("--- Anidación ---")
# Anicación 1
numero_1 = 20
numero_2 = 30

if numero_1 == 20:
    print(f"Numero_1 equivale a {numero_1}")
    if numero_2 == 30:
        print(f"Numero_2 equivale a {numero_2}")
print()

# Anidacion 2
nombre = "Pepe"
edad = 18

if nombre == "Pepe":
    if edad >= 18:
        print("Eres Pepe y ya puedes votar")
    else:
        print("Eres Pepe, pero no tienes edad para votar")
else:
    print("Tu no eres Pepe")
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
print("--- elif ---")
calificacion = float(input("Introduce tu calificación: "))
if calificacion == 10:
    print("Tu calificación es sobresaliente")
elif calificacion == 9:
    print("Tu calificación es notable")
elif calificacion == 8:
    print("Tu calificación es buena")
elif calificacion == 7:
    print("Tu calificación es suficiente")
elif calificacion <= 6:
    print("Tu calificación es insuficiente, no aprobaste")
else:
    print("Calificación fuera de rango")

print()

letra = input("Ingresa una letra: ")
# print(type(letra))
if letra.lower() == "a":
    print("Esta vocal es la a")
elif letra.lower() == "e":
    print("Esta vocal es la e")
elif letra.lower() == "i":
    print("Esta vocal es la i")
elif letra.lower() == "o":
    print("Esta vocal es la o")
elif letra.lower() == "u":
    print("Esta vocal es la u")
else:
    print("Tu letra es una consonante,un número o una cadena de caracteres")
print()
print("--- pass ---")
if True:
    pass  # Sirve para utilizar en un bloque de código vacío, no finaliza el código
    print("Continua el código...")
