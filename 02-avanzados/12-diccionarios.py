# Coleccion de datos con clave y valor
# La clave debe ser un string y el valor puede ser cualquier tipo de dato

# Podemos crear un diccionario vacio
diccionario = {}

# Podemos crear un diccionario con elementos
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Podemos acceder a los elementos de un diccionario
print(diccionario["clave1"])

# Podemos modificar un elemento de un diccionario
diccionario["clave1"] = "nuevo valor"
print(diccionario["clave1"])

# Podemos agregar un nuevo elemento al diccionario
diccionario["clave3"] = "nuevo valor"
print(diccionario)

# Podemos eliminar un elemento del diccionario
del diccionario["clave3"]
print(diccionario)

# Podemos iterar sobre un diccionario
for clave, valor in diccionario.items():
    print(clave, valor)

# Podemos convertir un diccionario en una lista
lista = list(diccionario.items())
print(lista)

# Podemos convertir una lista en un diccionario
diccionario = dict(lista)
print(diccionario)

# Podemos convertir un diccionario en una tupla
tupla = tuple(diccionario.items())
print(tupla)

# Podemos acceder a un elemento del diccionario con el metodo get()

print(diccionario.get("clave1"))

# Podemos evaluar si un elemento se encuentra en un diccionario con el metodo in

print("clave1" in diccionario)
