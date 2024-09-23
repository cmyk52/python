# Se define una funcion utilizando la plabra calve def
def hola():
    print("Hola funciones")


# Llamado a la funcion
hola()


# Funcion con parametros --> Los parametros son obligatorios
# Cuando definimos un parametro dentro de una funcion, le pasamos "ARGUMENTOS" al parametro.
def parametros(nombre):
    print(f"Bienvenido a las funciones con parametros {nombre}")


parametros("Jose")


# Pasando 2 Argumentos a una funcion con 2 Parametros
def parametros(nombre, apellido):
    print(f"Bienvenido a las funciones con parametros {nombre} {apellido}")


parametros("Jose", "Marambio")


# Argumentos opcionales a una funcion con 2 Parametros
# Es posible establecer un valor por defecto a los parametros opcionales usando "argumento por defecto". Si se pasa un argumento al parametro opcional usa el parametro indicado y no el parametro por defecto.
def parametros(nombre, apellido="Defecto"):
    print(f"Bienvenido a las funciones con parametros {nombre} {apellido}")


parametros("Jose")
parametros("Jose", "Marambio")

# Pasando argumentos en cualquier orden
# Se debe indicar a que corresponde cada argumento

parametros(apellido="Marambio", nombre="Pepe")

# Multiples argumentos (XARGS)
# Podemos pasar multiples argumentos, sin tener un limite maximo. Se define el argumento con un *
# Se iteran los argumentos y se guardan en una variable que imprimiremos al finalizar la operacion.
# Es necesario retroceder en la identacion para imprimirlos ya que de lo contrario, imprimira tantas veces pueda por cada argumento sin realizar la suma solicitada en la funcion.
# Identacion a la misma altura del bucle for


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3, 4)
suma(3, 4, 5)


# Argumentos empaquetados en un solo parametro(KWARGS)
# Se le indica al programa que debemos usar kwargs con dos simbolos **
# Siempre debemos darle el nombre del parametro


def lista(**datos):
    print(datos)
    print(datos["id"], datos["nombre"])


lista(id="1", nombre="jose")

# RETURN
# Nos sirve para obtener el valor devuelto por una funcion
# Para este caso, se obtiene el resultado de la suma de C y luego D, suma el resultado de C + 3 y lo imrprime


def suma(x, y):
    resultado = x + y
    return resultado


c = suma(2, 3)
d = suma(c, 3)
print(d)
