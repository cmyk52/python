# Las funciones MAP y FILTER generan lo mismo que las listas de comprension, sin embargo no puedens ser utilizadas a la vez.

# MAP

usuarios = [
    ["jose", 2],
    ["pedro", 1],
    ["daniel", 3],
    ["jimena", 5],
    ["marta", 4]
]


# Se usa el metodo map(funcion lambda, nombre de la nueva lista, indice de la posicion que queremos iterar, lista original que deseamos iterar)
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)


# FILTER
# Devuelve una lista con los elementos que cumplan la condicion.
filtrar = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(filtrar)
