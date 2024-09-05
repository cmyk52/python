texto = "Hola Mundo"
print(texto)

# Metodos
# Para llamar a un metodo debemos llamarlo agregando un simbolo de punto a la variable, el metodo y el simbolo ()

print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
# Remueve los espacios en blanco de nuestro string, rstrip() saca los de la derecha, lstrip los de la izquierda
print(texto.strip())

# Con el metodo find() podemos encontrar la posicion de un elemento dentro del string y los strings tienen su indice con base 0.
# Si no encuentra lo buscado en el indice, la respuesta sera indice -1
# Python es sencible a mayuzculas y minusculas, por lo cual es importante buscar con el texto bien escrito o transformarlo

print(texto.find("M"))
# Podemos buscar cadenas de texto, donde nos indica desde que indice comienza la cadena buscada
print(texto.find("Mun"))


# Con la palabra reservada in, podemos buscar un texto dentro de un string y nos devolvera como resultado un booleano (true, false)

print("Mun" in texto)


# Podemos con el metodo replace() reemplazar una cadena buscada  por un texto donde usaremos el metodo, sin embargo no muta la variable original, si no que sera asignada a una nueva variable.
nuevoTexto = texto.replace("Mund", "chanchito feliz")
print(texto, " - ", nuevoTexto)

# Escape, esta es una forma de indicar con el simbolo \ textos que lleven comillas en su interior

backslash = "Estos es un texto con \"Bakslash\""
print(backslash)
