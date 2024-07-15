print("--- Programa 1 ---")

# En el siguiente diccionario se  encuentran las principales capitales del mundo
# Se debe de realizar un programa que pida un país al usuario y muestre la capital
# del mismo, en caso de que no se encuentre el país en el diccionario se debe de
# mostrar un mensaje que indique que el país no se encuentra.

capitales_mundo = {
    "Alemania": "Berlín",
    "Francia": "París",
    "Italia": "Roma",
    "España": "Madrid",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres",
    "Rusia": "Moscú",
    "Canadá": "Ottawa",
    "Estados Unidos": "Washington D.C.",
    "México": "Ciudad de México",
    "Costa Rica": "San José",
    "El Salvador": "San Salvador",
    "Guatemala": "Ciudad de Guatemala",
    "Honduras": "Tegucigalpa",
    "Nicaragua": "Managua",
    "Panamá": "Ciudad de Panamá",
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago de Chile",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Perú": "Lima",
    "Venezuela": "Caracas",
    "Argelia": "Argel",
    "Egipto": "El Cairo",
    "Etiopía": "Adís Abeba",
    "Kenia": "Nairobi",
    "Nigeria": "Abuja",
    "Sudáfrica": "Pretoria (administrativa), Ciudad del Cabo (legislativa), Bloemfontein (judicial)",
    "China": "Pekín",
    "India": "Nueva Delhi",
    "Japón": "Tokio",
    "Corea del Sur": "Seúl",
    "Indonesia": "Yakarta",
    "Pakistán": "Islamabad",
    "Australia": "Canberra",
    "Nueva Zelanda": "Wellington",
}

pais = input("Ingresa el país del cual deseas saber su capital: ")

if pais.capitalize() in capitales_mundo:
    print(capitales_mundo[pais.capitalize()])
else:
    print("País no encontrado en el diccionario")
print()

print("--- Programa 2 ---")

# Se debe de crear un programa que pregunte al usuario por un número,
# el programa debe imprimir el jugador al que hace referencia ese número
# del siguiente diccionario

seleccion_alemania = {
    1: "Manuel Neuer",
    2: "Antonio Rüdiger",
    3: "Mats Hummels",
    4: "Matthias Ginter",
    5: "Jonas Hofmann",
    6: "Joshua Kimmich",
    7: "Kai Havertz",
    8: "Leon Goretzka",
    9: "Timo Werner",
    10: "Leroy Sané",
    11: "Thomas Müller",
    12: "Niklas Süle",
    13: "Matthias Ginter",
    14: "Florian Neuhaus",
    15: "Chrisopher Nkunku",
    16: "Lukas Klostermann",
    17: "Florian Wirtz",
    18: "Timo Werner",
    19: "Leroy Sané",
    20: "Joshua Kimmich",
    21: "Robin Gosens",
    22: "Marc-André ter Stegen",
    23: "Nico Schlotterbeck",
    24: "Emre Can",
    25: "Christian Günter",
    26: "Jamal Musiala",
    27: "Jule Kalidou Koulibaly",
}

numero_jugador = int(input("Ingresa el número del jugador: "))

if numero_jugador in seleccion_alemania:
    print(seleccion_alemania[numero_jugador])
else:
    print("El número no se encuentra dentro del diccionario")
