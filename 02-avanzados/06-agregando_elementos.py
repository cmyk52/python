animales = ["perro", "gato", "conejo", "pajaro", "pajaro"]

# Agregando elementos, debemos pasar el indice y el valor
animales.insert(2, "loro")

# agregando un elemento al final de la lista con append
animales.append("moco")

# Eliminando un elemento, no se indica el indice solo el valor
# Si existen elementos duplicados, solo elimina el primero
animales.remove("pajaro")

# Eliminando el ultimo elemento pop()
animales.pop()

# Tambien podemos pasar el indice del elemento que queremos eliminar con pop
animales.pop(2)


# Podemos eliminar elementos usando el indice del elemento que queremos eliminar
del animales[0]

# Limpiar completamente el arreglo

animales.clear()

print(animales)
