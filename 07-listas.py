array = ["Mi Piton", "My Java", "My PHP", "My JS", "My Ruby"]
print(array)
print(array[0])  # Accediendo a una posicion
# Muestra el ultimo elemento de la lista, en si lee la lista en sentido inverso por lo cual si usamos [-2] nos arroja "My JS"
print(array[-1])

# Modificando un elemento de la lista // Crea una nueva lista y no modifica la original
array[1] = "My Chela"
print(array)

# Podemos seleccionar un rango de elementos utilizando el simbolo : ,nos muestra desde el indice inicial hasta -1 del indice final
print(array[0:3])
# Si no pasamos el valor inicial, asume que se debe comenzar desde el indice 0
print(array[:3])
# Si no le pasamos el valor final, asume que se debe finalizar en el ultimo elemento del indice
print(array[0:])

# METODOS

# Podemos insertar elementos indicando el indice y luego el valor
array.insert(0, "My Go")
print(array)

# Podemos eliminar un elemento, solo indicando el valor sin el indice
array.remove("My Go")
print(array)

# Podemos evaluar si un elemento se encuentra en la lista usando la palabra reservada in, nos devuelve un booleano
print("My Chela" in array)

# Podemos el largo de nuestra lista(cuantos elementos contiene nuestra lista).
print(len(array))

array.clear()  # Podemos limpiar una lista con el metodo clear()
print(array)
