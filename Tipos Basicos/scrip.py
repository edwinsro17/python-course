#Tipos de datos basicos

#Variables 
nombreCompleto = "Edwin Rodriguez";  #String
edad = 19;                           #Integer
altura = 1.75;                       #Float
es_estudiante = True;    
mensaje =  f"Mi nombre es {nombreCompleto} tengo {edad} años de edad y mido {altura}"; #String formateado
print(mensaje);            #Booleano

#Metodos String
print(nombreCompleto.upper()); #Convierte el string a mayusculas
print(nombreCompleto.lower()); #Convierte el string a minusculas
print(nombreCompleto.split(" ")); #Convierte el string en una lista
print(nombreCompleto.replace("Edwin", "Chanchito")); #Reemplaza el string
print(nombreCompleto.find("Rodriguez")); #Devuelve la posicion de la primera ocurrencia del string
print(nombreCompleto.len()); #Devuelve la longitud del string
print(nombreCompleto.startswith("Edwin")); #Devuelve True si el string empieza con "Edwin"
print(nombreCompleto.endswith("Rodriguez")); #Devuelve True si el string termina con "Rodriguez"
print(nombreCompleto.isalpha()); #Devuelve True si el string solo contiene letras
print(nombreCompleto.isdigit()); #Devuelve True si el string solo contiene numeros
print(nombreCompleto.isspace()); #Devuelve True si el string solo contiene espacios
print(nombreCompleto.isalnum()); #Devuelve True si el string solo contiene letras y numeros
print(nombreCompleto.isupper()); #Devuelve True si el string solo contiene mayusculas
print(nombreCompleto.islower()); #Devuelve True si el string solo contiene minusculas

#Metodos Integer
print(edad.add(1)); #Suma el integer a 1
print(edad.subtract(1)); #Resta el integer a 1
print(edad.multiply(2)); #Multiplica el integer por 2
print(edad.divide(2)); #Divide el integer por 2
print(edad.modulo(2)); #Devuelve el modulo del integer
print(edad.power(2)); #Eleva el integer a la potencia de 2
print(edad.root(2)); #Devuelve la raiz del integer
print(edad.log(2)); #Devuelve el logaritmo del integer
print(edad.exp(2)); #Devuelve el exponencial del integer
print(edad.sin()); #Devuelve el seno del integer
print(edad.cos()); #Devuelve el coseno del integer
print(edad.tan()); #Devuelve la tangente del integer
print(edad.sqrt()); #Devuelve la raiz cuadrada del integer
print(edad.ceil()); #Devuelve el entero mas cercano al integer
print(edad.floor()); #Devuelve el entero mas cercano al integer
print(edad.round()); #Devuelve el entero mas cercano al integer
print(edad.abs()); #Devuelve el valor absoluto del integer
print(edad.max()); #Devuelve el valor maximo del integer
print(edad.min()); #Devuelve el valor minimo del integer
print(edad.sum()); #Devuelve la suma de los enteros
print(edad.avg()); #Devuelve la media de los enteros
print(edad.median()); #Devuelve la mediana de los enteros
print(edad.mode()); #Devuelve el modo de los enteros
print(edad.range()); #Devuelve el rango de los enteros
print(edad.std()); #Devuelve la desviacion estandar de los enteros
print(edad.var()); #Devuelve la varianza de los enteros
print(edad.percentile(50)); #Devuelve el percentil 50 de los enteros
print(edad.quantile(0.5)); #Devuelve el cuantil 0.5 de los enteros
print(edad.skewness()); #Devuelve la asimetria de los enteros
print(edad.kurtosis()); #Devuelve la curtosis de los enteros
print(edad.mad()); #Devuelve la desviacion media absoluta de los enteros

#Metodos Booleano
print(es_estudiante.__and__(True)); #Devuelve True si el booleano es True y el otro booleano es True
print(es_estudiante.__or__(False)); #Devuelve True si el booleano es True o el otro booleano es True
print(es_estudiante.__not__()); #Devuelve True si el booleano es False
print(es_estudiante.xor(True)); #Devuelve True si el booleano es True y el otro booleano es False
print(es_estudiante.xor(False)); #Devuelve True si el booleano es False y el otro booleano es True








