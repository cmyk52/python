lista = [1, 2, 3, 4]

print(*lista)  # con esto podemos desempaquetar una lista

# Desempaquetar una lista nos servira para ser utilizada en una funcion pasandole los elementos de la lista como argumentos


def n(n1, n2, n3, n4):
    print(n1, n2, n3, n4)


n(*lista)

# Convinar listas desempaquetandolas

listaDos = [5, 6, 7, 8]

nuevaLista = [*lista, *listaDos]
print(nuevaLista)
