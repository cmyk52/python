# Desempaquetar listas
# Nos sirve para guardar en variables cada uno de los elementos por separado de una lista

numeros = [1, 2, 3, 4, 5]
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Obteniendo un solo elemento
# Se usa con *para los demas numeros, iterando los elementos por separado a excepcion del primero
primero, *otros = numeros
print(primero, otros)  # (1, [2, 3])

# Obteniendo el primero y segundo elemento
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Obteniendo el primeor y el ultimo elemento
primero, *otros, ultimo = numeros
print(primero, otros, ultimo)
