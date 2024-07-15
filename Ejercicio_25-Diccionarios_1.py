# Colecciones desordenadas de pares clave-valor.
# Se utilizan para almacenar datos con una asociación entre claves y valores.
diccionario = {}
print(type(diccionario))
print(diccionario)

# Estructura clave:valor
# Las claves pueden ser números pero se puede volver confuso
resistencia = {
    "tipo": "resistencia",
    "valor": 1000,  # En ohms
    "tolerancia": "5%",
    "potencia": 0.25,  # En watts
    "paquete": "DIP",
    "marca": "Kachiquin",
}
print(resistencia)
print(resistencia["tolerancia"])
print(resistencia["valor"])
print(
    f'La {resistencia["tipo"]} tiene un valor de {resistencia["valor"]} ohms con una tolerancia de {resistencia["tolerancia"]}.'
)
print()
print("--- Mutabilidad ---")
resistencia["tolerancia"] = "1%"
print(resistencia)
print()
print("--- función del() ---")
del resistencia["marca"]
print(resistencia)
print("--- Manipulación ---")
ingredientes = {
    "Harina (kg)": 10,
    "Salsa (lt)": 2,
    "Queso mozarrella (kg)": 2,
    "Queso manchego (kg)": 1,
}
ingredientes["Salsa (lt)"] += 2
print(ingredientes["Salsa (lt)"])
print(ingredientes)
print(ingredientes["Queso mozarrella (kg)"] + ingredientes["Queso manchego (kg)"])
print()
print("--- Lectura secuencial ---")
for ingrediente in ingredientes:
    print(ingrediente)  # Devuelve las claves del diccionario
print()
for ingrediente in ingredientes:
    print(ingredientes[ingrediente])  # Devuelve los valores
print()
for ingrediente in ingredientes:
    print(ingrediente, ingredientes[ingrediente])  # Devuelve clave y valor
print()
for clave, valor in ingredientes.items():  # Uso del método .item()
    print(clave, valor)
print()
print("--- Diccionarios anidados---")

Aragorn = {
    "nombre": "Aragorn",
    "clase": "Guerrero",
    "raza": "Humano",
    "nivel": 10,
    "atributos": {
        "fuerza": 18,
        "destreza": 14,
        "constitucion": 16,
        "inteligencia": 12,
        "sabiduria": 14,
        "carisma": 16,
    },
    "habilidades": ["Espada a dos manos", "Escudo", "Liderazgo"],
    "equipo": {
        "arma": "Espada de Gondor",
        "armadura": "Armadura de mithril",
        "escudo": "Escudo de Rohirrim",
    },
    "historia": "Hijo del jefe de los Dunedain, Aragorn está destinado a reclamar el trono de Gondor.",
}
print(Aragorn)
print(Aragorn["atributos"])
print(Aragorn["atributos"]["inteligencia"])
print()
fuerza_aragorn = Aragorn["atributos"]["fuerza"]
print(f"La fuerza de Aragorn es: {fuerza_aragorn}")
print()
atributos_aragorn = Aragorn.get("atributos")  # función get()
print(f"Los atributos de Aragorn son: {atributos_aragorn}")
frase = "La raza de Aragorn es: {raza}".format(
    **Aragorn
)  # Usar str.format() para eliminar las llaves
print(frase)
print()
sabiduria_aragorn = Aragorn.get("atributos").get("sabiduria")
print(f"La sabiduría de Aragorn es: {sabiduria_aragorn}")
sabiduria_aragorn = Aragorn.get("atributos", {}).get("sabiduria", 0)
print(f"La sabiduría de Aragorn es: {sabiduria_aragorn}")
velocidad_aragorn = Aragorn.get("atributos", {}).get(
    "velocidad", 0
)  # Elemento no existente en el diccionario
print(velocidad_aragorn)
escudo_aragorn = Aragorn.get("escudo", {}).get(
    "nivel", "No existente"
)  # Elemento no existente en el diccionario
print(escudo_aragorn)
