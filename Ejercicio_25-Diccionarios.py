diccionario = {}
print(type(diccionario))
print(diccionario)

# Estructura clave:valor
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
print(f'La {resistencia["tipo"]} tiene un valor de {resistencia["valor"]} ohms con una tolerancia de {resistencia["tolerancia"]}.')