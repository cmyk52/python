n1 = input("Ingresa un numero: ")
n2 = input("Ingresa otro numero: ")

suma = int(n1) + int(n2)
resta = int(n1) - int(n2)
multiplicacion = int(n1) * int(n2)
division = int(n1) / int(n2)

# Podemos trabajar con string y concatenacion, deberemos usar la letra f y 3 comillas > mensaje {variable} > 3 comillas
mensaje = f"""

Para el calculo de {n1} y {n2}, los resultados son:

suma es {suma},
resta es {resta},
division es {division},
multiplicacion es {multiplicacion}



"""

print(mensaje)
