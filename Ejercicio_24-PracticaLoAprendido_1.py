"""
Codifica un programa que lea 2 números (entero o float) por teclado y permita elegir entre 4 opciones en un menú:

- Imprimir la suma de los dos números.
- Imprimir la resta de los dos números (el primero menos el segundo).
- Imprimir la multiplicación de los dos números.
- Imprimir el módulo de los dos números.

En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""
print('--- Programa 1 ---')
while True:
    numero_1=float(input('Ingresa el primer número: '))
    numero_2=float(input('Ingresa el segundo número: '))
    print('--- MENÚ ---')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. Módulo')
    opcion=(int(input('Ingresa una opción: ')))
   
    if opcion==1:
        suma=numero_1+numero_2
        print(f'La suma de los dos números es: {suma}\n')
        #break
    elif opcion==2:
        resta=numero_1-numero_2
        print(f'La resta de los dos números es: {resta}\n')
        #break
    elif opcion==3:
        multiplicacion=numero_1*numero_2
        print(f'La multiplicación de los dos números es: {multiplicacion}\n')
        #break
    elif opcion==4:
        modulo=numero_1%numero_2
        print(f'El módulo de los dos números es: {modulo}\n')
        #break
    else:
        print('No ha ingresado una opción válida.\n')