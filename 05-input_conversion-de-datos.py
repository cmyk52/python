# Podemos capturar un input realizado por un usuario con el metodo input y guardarlo en una variable.

variable = input("Ingresa tu edad:")
print(variable) 
print(type(variable)) # Podemos verificar el tipo de dato guardado en la variable con el metodo type(variable)

# Para este caso nos guarda el dato como tipo de dato string

# Para transformar datos podemos utilizar metodos indicando a que tipo de datos vamos a transformar
numero = int(variable) # En este caso usamos int() para transformar en numero la variable llamada variable
print(numero + 22)

string = str(22) # Transformamos un numero a string
float = float("22.13") # Transformamos un string a float
boolean = bool("poto") # Transformamos un datos a booleano, en la mayoria de las ocasiones lo transforma en true

# Solo se transformara en falso:
# Un string con la palabra False
# Un int con el valor 0
# Un string vacio: " "
# Un objeto None

print(type(string))
print(type(float))
print(type(boolean))
print(boolean == True)