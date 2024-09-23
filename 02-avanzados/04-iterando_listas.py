mascotas = ["perro", "gato", "conejo", "pajaro"]

# Se puede iterar una lista, un string y range
# No podemos ingresar al indice de mascotas usando for, por lo cual sera necesario realizar una funcion iterable
for mascota in mascotas:
    print(mascota)

# Funcion iterable
# Esto devuelve el indice y el valor // ESTO ES CONOCIDO COMO UNA "TUPLA"
for mascotas in enumerate(mascotas):
    print(mascotas)

# Podemos empaquetar cada elemento de mascotas en una variable

animales = ["perro", "gato", "conejo", "pajaro"]
primero, segundo, *otros = mascotas

for indice, animales in enumerate(animales):
    print(indice, animales)
    break
