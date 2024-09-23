numeros = [2, 10, 1986, 32]

# SORT ordenamos el elemento de menor a mayor
numeros.sort()

# SORT ordenamos los elementos de mayor a menor en la misma lista
numeros.sort(reverse=True)

# SORTED ordenamos el elemento de menor a mayor en una nueva lista
sorted(numeros)

print(numeros)

# Ordenando listas complejas
usuarios = [
    ["jose", 2],
    ["jose", 1],
    ["jose", 3],
    ["jose", 5],
    ["jose", 4],
    ["jose", 6],
    ["jose", 7],
    ["jose", 8]
]


def ordenar(elemento):
    return elemento[1]


# Podemos ordenar con el metodo sort, sin embargo deberemos pasarle una funcion donde los argumentos para ordenar seran la posicion del indice del elemento que queremos ordenar.
usuarios.sort(key=ordenar, reverse=True)
print(usuarios)


# FUNCIONES LAMBDA O ANONIMAS

# Podemos pasar una funcion lambda o anonima como parametro de un metodo sort, donde tendremos que pasar el parametro(elemento por ej) y el indice del elemento por el cual queremos ordenar.
# usuarios.sort(key=lambda parametro:retorno reverse=True)

usuarios.sort(key=lambda elemento: elemento[1])
print(usuarios)
