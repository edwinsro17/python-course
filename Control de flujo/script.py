#if else y el elif

#En este script vamos a ver como usar el if else para tomar decisiones en nuestro codigo

#Ejemplo practico 1: Crear un programa que pida al usuario ingresar su edad y luego le diga si es mayor de edad o no

edad = int(input('Ingrese su edad: '));
if edad >=18:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')

#Ejemplo practico 2: Crea una caoculadora basica que le permita al susuario hacer suma, resta, multiplicación y divición
print('Bienvenido a tu calculadora X');
numero1=int(input('Por favor ingresa el primer numero: '));
numero2=int(input('Por favor ingresa el segundo numero: '));
print('Escrive el numero de la operacion o acción que deseas realizar');
operacion = int(input('1. Suma 2. Resta. 3. Multiplicación 4. División, 5. Salir : '));

if operacion == 1:
    print('El resultado de la suma de los dos numeros que ingreso es: ', numero1 + numero2)
elif operacion == 2:
    print('El resultado de la resta de los dos numeros que ingreso es: ', numero1 - numero2)
elif operacion == 3:
    print('El resultado de la multiplicación de los dos numeros que ingreso es: ', numero1 * numero2)
elif operacion == 4:
    print('El resultado de la división de los dos numeros que ingreso es: ', numero1 / numero2)
elif operacion == 5:
    print('Hasta luego fue un gusto ayudarte ;)')
    exit();
else:
    print('Por favor ingrese un numero valido')





