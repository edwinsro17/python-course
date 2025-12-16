# Cree un programa que permita al usuario ingresar un número entero menor que 5.
# a partir de ese número, el programa debe contar e imprimir la cantidad de vueltas que da una pelota, 
# numerándolas consecutivamente hasta llegar a la vuelta número 10.
# Si el usuario ingresa un número mayor o igual a 5, el programa debe mostrar un mensaje indicando que el número no es válido.
numero = int(input('Ingrese un numero menor al 5: '))
if(numero < 5):
    while numero <= 10 :
        print('Vuelta', numero, 'de pelota')
        numero +=1
else:
    print('Por favor igrese un numero menor a 5')

