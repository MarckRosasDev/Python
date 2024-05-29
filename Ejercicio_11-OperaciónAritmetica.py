# NOTA: Hay diversas formas de solucionar los problemas planteados, elige la que más te agrade.
"""
    EJERCICIO 1:
Escribe un programa que reallice la siguiente operación:

((3+2)/(2*5))^2

"""

print("EJERCICIO 1")
print(
    "El resultado de la operación ((3+2)/(2*5))^2 es: "
    + str(((3 + 2) / (2 * 5)) ** 2)
    # pow(((3 + 2) / (2 * 5)),2)
)
print("------------")

"""
    EJERCICIO 2:
Los dos productos más vendidos de una tienda de electrónica son: Kit Arduino Uno y tarjeta Arduino Uno.
Se suele vender por su página de internet y la empresa de logística les cobra por peso de cada paquete, por
lo que se debe de calcular el peso de cada paquete teniendo en cuenta que el kit Arduino Uno tiene un peso
de 250 gramos y la tarjeta Arduino Uno de 24 gramos, respectivamente. Un cliente solicita la cantidad de 12
kits de Arduino Uno y 35 Tarjetas Arduino Uno. Realiza un programa que muestre el peso total de la venta en
kilogramos.

"""
print("EJERCICIO 2")
peso_kit_arduino = 250
peso_arduino = 24
peso_paquete = ((peso_kit_arduino * 12) + (peso_arduino * 35)) / 1000
print("El peso total del paquete es: " + str(peso_paquete) + " Kg")
print("------------")

"""
    EJERCICIO 3:
Un cocinero necesita comprar los siguientes productos:
5 Kg de Harina.
3 Kg de queso mozarrella.
3 Kg de queso gouda.
2 KG de queso cheddar.
4 Kg de peperoni.
2 botellas de acete de olivo de 1 lt cada una.
10 Kg de tomate.

Crea un programa en el que se ingresen los precios de cada producto por medio de consola, se debe
calcular el subtotal y el costo total. Los precios de los productos son los siguientes:
1 Kg de Harina - $20.00
1 Kg de queso mozarrella - $260.00
1 Kg de queso gouda - $250.00
1 Kg de queso cheddar - $240.00
1 Kg de pepperoni - $400.00
1 Litro de aceite de oliva - $260.00
1 Kg de tomate - $35.00

"""
print("EJERCICIO 3")
precio_harina = int(input("Introduce el precio de la harina por kilogramo: "))
cantidad_harina = int(input("¿Cuánta harina necesitas (Kg.)?: "))

precio_mozarrealla = int(
    input("Introduce el precio del queso mozarrella por kilogramo: ")
)
cantidad_mozarrella = int(input("¿Cuánto queso mozarrella necesitas (Kg.)?: "))

precio_gouda = int(input("Introduce el precio del queso gouda por kilogramo: "))
cantidad_gouda = int(input("¿Cuánto queso gouda necesitas (Kg.)?: "))

precio_cheddar = int(input("Introduce el precio del queso cheddar por kilogramo: "))
cantidad_cheddar = int(input("¿Cuánto queso cheddar necesitas (Kg.)?: "))

precio_pepperoni = int(input("Introduce el precio del pepperoni por kilogramo: "))
cantidad_pepperoni = int(input("¿Cuánto pepperoni necesitas (Kg.)?: "))

precio_aceite_oliva = int(input("Introduce el precio del aceite de oliva por litro: "))
cantidad_aceite_oliva = int(input("¿Cuánto aceite de oliva necesitas (Lt.)?: "))

precio_tomate = int(input("Introduce el precio del tomate por kilogramo: "))
cantidad_tomate = int(input("¿Cuánto tomate necesitas (Kg.)?: "))

subtotal_harina = precio_harina * cantidad_harina
subtotal_mozarrella = precio_mozarrealla * cantidad_mozarrella
subtotal_gouda = precio_gouda * cantidad_gouda
subtotal_cheddar = precio_cheddar * cantidad_cheddar
subtotal_pepperoni = precio_pepperoni * cantidad_pepperoni
subtotal_aceite_oliva = precio_aceite_oliva * cantidad_aceite_oliva
subtotal_tomate = precio_tomate * cantidad_tomate

total = (
    subtotal_harina
    + subtotal_mozarrella
    + subtotal_gouda
    + subtotal_pepperoni
    + subtotal_cheddar
    + subtotal_aceite_oliva
    + subtotal_tomate
)

print('El subtotal del costo de la harina es: '+str(subtotal_harina))
print('El subtotal del costo del queso mozarrella es: '+str(subtotal_mozarrella))
print('El subtotal del costo del queso gouda es: '+str(subtotal_gouda))
print('El subtotal del costo del queso cheddar es: '+str(subtotal_cheddar))
print('El subtotal del costo del pepperoni es: '+str(subtotal_pepperoni))
print('El subtotal del costo del aceite de oliva es: '+str(subtotal_aceite_oliva))
print('El subtotal del costo del tomate es: '+str(subtotal_tomate))
print("")
print('El total de la compra es de: '+str(total))
print("------------")
