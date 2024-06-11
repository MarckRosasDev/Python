print('--- While ---')
contador = 0
while contador <=19:
    #contador = contador+1
    contador+=1
    print(f'Contador vale: {contador}')
print()  

print('--- While con else ---')
contador=0
while contador <=10:
    contador+=1
    print(f'Contador vale: {contador}')
else:
    print(f'Iteraciones completadas, contador vale {contador}')
print()

print('--- While con break ---')
contador=0
while contador <=30:
    contador+=1
    if(contador == 10):
        print(f'Se rompe el bucle cuando contador vale {contador}')
        break    
    print(f'Contador vale: {contador}')
else:
    print(f'Iteraciones completadas, contador vale {contador}')
print()

print('--- While con continue ---')
contador=0
while contador <=15:
    contador+=1
    if(contador == 3 or contador==10):
        print(f'El bucle continúa, contador vale {contador}')
        continue   
    print(f'Contador vale: {contador}')
else:
    print(f'Iteraciones completadas, contador vale {contador}')