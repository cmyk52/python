mascotas = ["perro", "gato", "conejo", "pajaro"]

print(mascotas)

# Acceder un elemento de la lista
print(mascotas[0])

# Acceder el ultimo elemento de la lista
print(mascotas[-1])

# cambiando un elemento de la lista
mascotas[0] = "loro"
print(mascotas)

# Eliminando un elemento de la lista
mascotas.remove("conejo")

# accediendo a un rango de elementos de la lista
print(mascotas[0:3])

# Accediendo a un indice saltando el primer elemento

print(mascotas[::2])  # saltando de 2 en 2
print(mascotas[1::2])  # saltando de 2 en 2, comenzando del indice 1

# Obteniendo elementos impares
numeros = list(range(21))
print(numeros[1::2])  # comienza del indice 1 de la lista, saltando de 2 en 2

# Obteniendo elementos pares
print(numeros[::2])  # comienza del indice 0 de la lista, saltando de 2 en 2

# Revertir una lista
mascotas.reverse()
print(mascotas)
