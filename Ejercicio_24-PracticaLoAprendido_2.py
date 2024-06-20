
print("--- Programa 8 ---")

# En la siguiente lista ['Intensidad', 1000, "LED", 'Raspberry Pi', 1234, 'Hipotenusa'],
# Se debe hacer un programa que muestre los valores de esa lista, además, debe pedir dos
# datos y esos que sean ingresados deben ser sustituidos en el primer y último lugar:
# El pimer dato debe ser de tipo int y el último de tipo string 
datos=['Intensidad', 1000, "LED", 'Raspberry Pi', 12.34, 'Hipotenusa']

primer_dato=int(input('Ingresa el primer valor (int): '))
ultimo_dato=input('Ingresa el ultimo valor (str): ')

print(datos)

datos[0]=primer_dato
datos[-1]=ultimo_dato

print(datos)