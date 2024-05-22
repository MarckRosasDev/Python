num_1 = 68  # int (entero)
num_2 = 23.78  # float (flotante)

print(num_1)
print(type(num_1))
print(type(float(num_1)))  # Convertir numero 1 a flotante e imprimirlo en pantalla
print("---")

print(num_2)
print(type(num_2))
print(int(num_2))  # Convertir numero 1 a flotante e imprimirlo en pantalla
print(type(num_2))  # La varible no se almacena como entero ya que no se ha almacenado en la misma varibla o en alguna otra
print("---")
num_2 = int(num_2)  # Aquí se almacena la conversión de float a int, no se redondea sólo se mantiene la parte entera
print(num_2)
print(type(num_2))
