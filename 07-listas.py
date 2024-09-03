array = ["Mi Piton", "My Java", "My PHP", "My JS", "My Ruby"]
print(array)
print(array[0]) # Accediendo a una posicion
print(array[-1]) # Muestra el ultimo elemento de la lista, en si lee la lista en sentido inverso por lo cual si usamos [-2] nos arroja "My JS"

array[1] = "My Chela" # Modificando un elemento de la lista // Crea una nueva lista y no modifica la original
print(array)

print(array[0:3]) # Podemos seleccionar un rango de elementos utilizando el simbolo : ,nos muestra desde el indice inicial hasta -1 del indice final
print(array[:3]) # Si no pasamos el valor inicial, asume que se debe comenzar desde el indice 0
print(array[0:]) # Si no le pasamos el valor final, asume que se debe finalizar en el ultimo elemento del indice

# METODOS

array.insert(0, "My Go") # Podemos insertar elementos indicando el indice y luego el valor
print(array)

array.remove("My Go") # Podemos eliminar un elemento, solo indicando el valor sin el indice
print(array)

print("My Chela" in array) # Podemos evaluar si un elemento se encuentra en la lista usando la palabra reservada in, nos devuelve un booleano

print(len(array)) # Podemos el largo de nuestra lista(cuantos elementos contiene nuestra lista). 

array.clear() # Podemos limpiar una lista con el metodo clear()
print(array)