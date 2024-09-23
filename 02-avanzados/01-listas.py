numeros = [1, 2, 3]
letras = ["a", "b", "c"]

print(numeros)
print(letras)


# Podemos crear un arreglo que contenga el mismo valor en todos sus elementos
ceros = [0] * 5  # [0, 0, 0, 0, 0]
print(ceros)

# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], cada elemento se multiplicara 5 veces
ceros_y_unos = [0, 1] * 5
print(ceros_y_unos)


# Podemos unir 2 listas
alfanumerico = numeros + letras
print(f"Este es el alfanumerico: {alfanumerico}")

# Crear una lista con 10 elementos utilizando un iterable (Se utiliza la funcion list() para crear listas y el iterable se define como parametro de la funcion)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - Esto es un iterable que contara de 0 a 9
rango = list(range(1, 11))
print(f"Esto esun iterable que contara de 1 a 10: {
      rango} y crea una lista con estos elementos")

# Podemos crear una lista con un iterable string
chars = list("hola")
print(chars)

# MATRIZ
# dentro de las listas podemos guardar otras listas, a esto se le conoce como una matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
