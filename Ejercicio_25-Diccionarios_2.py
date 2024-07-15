print("--- Métodos en diccionarios ---")

Caricatura = {
    "nombre": "Félix el Gato",
    "especie": "Gato",
    "apariencia": {
        "color": "Negro",
        "ojos": "Blancos y grandes",
        "boca": "Amplia con sonrisa pícara",
        "cola": "Larga y delgada",
        "cuerpo": "Flexible y ágil",
    },
    "personalidad": {
        "travieso": True,
        "juguetón": True,
        "ingenioso": True,
        "astuto": True,
        "optimista": True,
        "alegre": True,
        "servicial": True,
        "torpe": True,
    },
    "habilidades": {
        "agilidad": "Alta",
        "acrobacias": True,
        "trucos": True,
        "cola_herramienta": True,
        "bolsas_magicas": True,
        "resolucion_problemas": "Creativa e ingeniosa",
    },
    "frases_celebres": [
        "¡Ay, caramba!",
        "¡Miau!",
        "¡No puedo creerlo!",
        "¡Esto sí que es un lío!",
        "¡Estoy bien, estoy bien!",
    ],
    "relaciones": {
        "villanos": ["Profesor Wacko", "Poindexter"],
        "amigo_humano": "Dick Tracy",
        "compañeros": "Otros gatos o animales",
    },
}
print(Caricatura.keys())
print(Caricatura.values())
print()
Caricatura["En emisión"] = False  # Adicionar información al diccionario
print(Caricatura)
print()
pares = Caricatura.items()  # Obtiene una vista de los pares clave-valor del diccionario
print(f"Pares claves-valor: {pares}")
print()
nombre = Caricatura.get("nombre", "No existe")
print(f"El nombre del gato es: {nombre}")
print()
existe_nombre = (
    "nombre" in Caricatura
)  # Verifica si una clave específica existe en el diccionario.
existe_nombre_1 = "Nombre" in Caricatura
print(f'Existe la clave "nombre": {existe_nombre}')
print(f'Existe la clave "Nombre": {existe_nombre_1}')
print()
diccionario = {"nombre": "Bit", "edad": 30}
datos_nuevos = {"ciudad": "CDMX", "ocupacion": "Programador"}
diccionario.update(
    datos_nuevos
)  # Actualiza el diccionario con pares clave-valor de otro diccionario o un objeto
print(f"Diccionario actualizado: {diccionario}")
print()
ciudad = diccionario.pop(
    "ciudad"
)  # Elimina un elemento del diccionario por su clave y devuelve el valor asociado.
print(f"Ciudad eliminada: {ciudad}")
print(f"Diccionario actualizado: {diccionario}")
print()
diccionario.clear()  # Elimina todos los elementos del diccionario.
print(f"Diccionario después de limpiar: {diccionario}")
print()
cantidad_elementos = len(
    Caricatura
)  # Devuelve la cantidad de elementos (pares clave-valor) en el diccionario.
print(f"Cantidad de elementos en el diccionario: {cantidad_elementos}")
print()
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Ciudad de México"}
copia_diccionario = (
    diccionario.copy()
)  # Crea una copia superficial del diccionario. Los cambios en la copia no afectan al original.
copia_diccionario["ciudad"] = "Guadalajara"
print(f"Diccionario original: {diccionario}")
print(f"Copia del diccionario: {copia_diccionario}")
