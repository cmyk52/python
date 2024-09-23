# Significa grupo o conjunto de elementos unicos
# coleccion de datos que no se puede repetir y no esta ordenada, tampoco podemos acceder a sus elementos por indice
# Podremos utilizar funciones que modifiquen los sets

primer = {1, 1, 2, 3, 3, 4}


# Convertir una lista en un set

segundo = [3, 4, 5, 6, 7]
segundo = set(segundo)

print(segundo)

# Podemos unir sets con operador union |
print(primer | segundo)

# Operador Interseccion (Nos devuelve los elementos comunes)
# En este caso nos devolvera 3 y 4 de los sets primer y segundo, porque son los elementos comunes
print(primer & segundo)

# Operador de diferencia (Mostra los elementos de primer que no estan en segundo)
print(primer - segundo)

# Operador diferencia simetrica (Nos devuelve los elementos que se encuentren entre el primer y el segundo, pero no en ambos) - elimina duplicados entre ambos sets
print(primer ^ segundo)

# Podemos consultar si un elemento se encuentra en un set
print(3 in primer)
print(3 in segundo)
