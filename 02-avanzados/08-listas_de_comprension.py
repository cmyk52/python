
usuarios = [
    ["jose", 2],
    ["pedro", 1],
    ["daniel", 3],
    ["jimena", 5],
    ["marta", 4]
]

# Estas se generan similar a un for pero con menos lineas de codigo
# Indicamos lo que queremos que nos retorne y posicion del indice que iteramos y , el nombre que le pondremos a lo iterado y donde estaremos iterando.
nombres = [usuario[0] for usuario in usuarios]
print(nombres)


# Esto es similar a un ciclo for
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


# Filtrar
# Eliminamos el indice y generamos una condicional if al final
# Para este caso solo queremos los nombres que tengan un indice mayor a 2

nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)


# Es posible filtrar y transformar a la vez una lista
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
