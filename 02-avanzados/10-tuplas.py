# Una tupla es una lista que no se puede modificar
# Se pueden crear nuevas tuplas de una tupla, sin modificar la ya existente
# (Estas las usaremos cuando no queramos de forma accidental modificar un elemento de un listado)
# No podremos usar append() o pop() para modificar una tupla

numeros = (1, 2, 3)

# Podemos concatenar tuplas
numeros = numeros + (4, 5, 6)

print(numeros)

# Podemos transformar un listado a una tupla
# con la funcion tuple([recibe cualquier iterable])

punto = tuple([1, 2])
stringtupla = tuple("hola")

print(punto)
print(stringtupla)

# Podemos acceder a un numero limitado de elementos de una tupla indicando la cantidad de elementos de la tupla

print(stringtupla[:2])

# Desempaquetar las tuplas

primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Podemos iterar una tupla

for numero in numeros:
    print(numero)

# Podemos crear una lista de una tupla
# Con esto la podemos modificar.

lista = list(numeros)
print(lista)
