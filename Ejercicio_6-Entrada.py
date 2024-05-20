nombre = input("Escribe tu nombre: ")
print("Tu nombre es: " + nombre)
print(type(nombre))

edad = input("Escribe tu edad: ")
altura = input("Escribe tu altura: ")
print("Tu edad es: " + edad)
print(type(edad))
print("Tu altura es: " + altura)
print(type(altura))

tacos = int(input("Ingresa la cantidad de tacos que comes: "))
print(type(tacos))
print("Comes " + str(tacos) + " tacos")
print(type(tacos))

mas_tacos = int(input("¿Cuántos tacos quieres agregar a tu orden: "))
total_tacos = mas_tacos + tacos
print("Pediste " + str(tacos) + "\ny agregaste " + str(mas_tacos))
print("\t¡Te has comido " + str(total_tacos) + " con todo, Chanchito!")

peso = float(input("Ingresa tu peso en kg: "))
print(type(peso))
peso_tacos = 1.2
peso = peso + peso_tacos
print("Comiste muchos tacos y ahora pesas " + str(peso) + "kilogramos")
