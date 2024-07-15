# Colecciones desordenadas de elementos únicos.
# Se utilizan para almacenar conjuntos de datos sin duplicados.

conjunto = set()
print(type(conjunto))

conjunto_ciudades = {
    "Xalapa",
    "Veracruz",
    "Papantla",
    "Coatzacoalcos",
    "Tuxpan",
    "Catemaco",
    "Papantla",
}
print(conjunto_ciudades)
print()
conjunto_numeros = {100, 200, 300, 400, 100}
print(conjunto_numeros)
print()
conjunto_tipos = {True, 2024, 1.16, "Python"}
print(conjunto_tipos)
print()
conjunto_desde_cadena = set("Transistor")
print(conjunto_desde_cadena)
print()
conjunto_desde_tuplas = set(
    ("Zacahuilt", "Molotes", "Bocoles", "Zacahuilt", "Molotes", "Estrujada")
)
print(conjunto_desde_tuplas)
print()
lista_numeros = [
    100,
    200,
    300,
    500,
    100,
    200,
    1000,
    600,
    200,
    700,
    400,
    500,
    800,
    900,
    50,
    300,
]
conjunto_lista_numeros = set(lista_numeros)  # Convertir lista a conjunto
print(conjunto_lista_numeros)
numeros_sin_repetir = list(conjunto_lista_numeros)  # Convertir conjunto a lista
print(numeros_sin_repetir)
print()
longitud_ciudades = len(conjunto_ciudades)  # Longitud del conjunto
print(longitud_ciudades)
print()
print("Xalapa" in conjunto_ciudades)  # Busca si un elemento se encuentra en el conjunto
print("Papantla" in conjunto_ciudades)
print("CDMX" in conjunto_ciudades)
print()
conjunto_ciudades.add("CDMX")
print(conjunto_ciudades)
conjunto_ciudades.add("CDMX")  # No se permite agregar elementos repetidos
print(conjunto_ciudades)
print()
conjunto_ciudades.update(
    {"Cordoba", "Tulum", "Champotón"}
)  # Actualizar datos al conjunto
print(conjunto_ciudades)
print()
conjunto_ciudades.remove("Champotón")  # Remover elemento del conjunto
print(conjunto_ciudades)
conjunto_ciudades.remove("Xalapa")
print(conjunto_ciudades)
# conjunto_ciudades.remove('catemaco')
conjunto_ciudades.discard("catemaco")
print(conjunto_ciudades)
conjunto_ciudades.discard("Catemaco")
print(conjunto_ciudades)
conjunto_ciudades.add("Catemaco")  # Agregar elemento al conjunto
print(conjunto_ciudades)
print()
conjunto_ciudades.clear()  # Limpiar todo el conjunto
print(conjunto_ciudades)
