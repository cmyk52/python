# Podemos almacenar el valor un input realizado por un usuario con el metodo input y guardarlo en una variable.

variable = input("Ingresa tu edad:")
print(variable)
# Podemos verificar el tipo de dato guardado en la variable con el metodo type(variable)
print(type(variable))

# Para este caso nos guarda el dato como tipo de dato string

# Para transformar datos podemos utilizar metodos indicando a que tipo de datos vamos a transformar
# En este caso usamos int() para transformar en numero la variable llamada variable
numero = int(variable)
print(numero + 22)

string = str(22)  # Transformamos un numero a string
float = float("22.13")  # Transformamos un string a float
# Transformamos un datos a booleano, en la mayoria de las ocasiones lo transforma en true
boolean = bool("poto")

# Solo se transformara en falso:
# Un string con la palabra False
# Un int con el valor 0
# Un string vacio: " "
# Un objeto None

print(type(string))
print(type(float))
print(type(boolean))
print(boolean == True)
