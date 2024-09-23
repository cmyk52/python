# El scope en Python, es asignado dependiendo de la altura donde fue definida una variable y el bloque donde se esta ejecutando.
# Es posible crear 2 variables con el mismo nombre, siempre y cuando esten en diferentes bloques.

# En este caso el scope de la variable saludo es de la funcion holaMundo y se logra imprimir
def holaMundo():
    saludo = "hola mundo"
    print(saludo)


holaMundo()

# En este caso se intenta imprimir la variable saludo fuera del bloque o altura de la funcion, por lo cual no se imprime.


def holaChanchito():
    saludo = "hola chanchito"


# print(saludo)  # Queda como undefined


# GLOBAL
# Se puede acceder a la variable desde cualquier parte del programa
# Se puede acceder a la variable desde cualquier parte del programa, ya sea en el mismo archivo o en otro.
saludaGlobal = "hola mundo global"
print(saludaGlobal)
