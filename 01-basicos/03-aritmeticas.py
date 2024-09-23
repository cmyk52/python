import math  # Modulo nativo de Python para trabajar con aritmetica.

# Podemos realizar operaciones aritmeticas, similar a como lo realizamos en una calculadora

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)  # Se utiliza ** para realizar potencias(un numero elevado a su potencia)
print(5 % 2)  # Se utiliza % para realizar el modulo o sobrante(es lo que resta de una division entre 2 numeros)

# Podemos realizar operaciones utilizando la variable seguido de * - + / luego es = y el multiplicador, resta, etc....
numero = 2

numero *= 5
print(numero)


# Metodo Round, redondeara un numero

print(round(1.3))

# Metodo Abs, nos entrega un numero absoluto siempre en positivo

print(abs(-1.3))

#########################################
# Trabajando con el modulo nativo Math
# https://docs.python.org/3/library/math.html

print(math.ceil(1.3))  # Llevara el numero al entero superior mas cercano
print(math.floor(1.99))  # Llevara el numero al entero inferior mas cercano
# print(math.isnan("poto")) # Indica en booleano si el valor no es numero como True, en caso que si sea numero indica False

# Nos permite realizar potencias, en este caso 3 elevado a 2
print(math.pow(3, 2))
print(math.sqrt(9))  # Nos permite realizar raices, en este raiz de 3
