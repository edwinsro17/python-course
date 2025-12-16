
opcion = int(input('Ingrese el numero de la pelota (1-3): 2'))
match opcion:
        case 1:
            print('Pelota pequeña')
        case 2:
            print('Pelota mediana')
        case 3: 
            print('Pelota grande');
        case _:
            print('Por favor ingrese un numero valido')

