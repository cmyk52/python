# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
# print("Hola Mundo")

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

# saludo = input("Ingresa hola mundo!")
# print(saludo)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

# nombre = input("Ingresa tu nombre")
# print(f"Hola {nombre}")

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

# resultado = ((3+2)/(2*5))**2
# print(resultado)


# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# trabajadas = int(input("Ingresa la cantidad de horas trabajadas: "))
# coste = int(input("Ingresa el corte de una hora trabajada: "))

# valor = trabajadas * coste
# print(f"Trabajaste {trabajadas} hrs, las cuales tienen un coste de {coste}, el total del importe es {valor}")


# Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n*(n+1))/2

# n = int(input("Ingresa un numero entero: "))
# sumar = 1
# while sumar <= n:
#     print(sumar)
#     sumar = sumar + 1

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# peso = int(input("Ingresa tu peso en Kg"))
# altura = int(input("Ingresa tu altura en Metros"))

# imc = (altura*2)/peso
# print(f"Tu índice de masa corporal es {imc} donde {imc} es el índice de masa corporal calculado redondeado con dos decimales")

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# capital = int(input("Ingresa un monto capital a invertir"))
# interes = int(input("Ingresa la tasa de interes anual"))
# periodo = int(input("Ingresa cuantos anhos se invertira el dinero"))

# interesAcumulado = ((interes * capital) / 100) * periodo

# capitalTotal = interesAcumulado + capital
# print(capitalTotal)

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

# payasosVendidos = 10
# munecasVendidas = 10
# pesoPayaso = 112
# pesoMuneca = 75

# totalPesoPayasos = (payasosVendidos * pesoPayaso) / 1000
# totalPesoMuneca = (munecasVendidas * pesoMuneca) / 1000

# print(f"""

# Se vendieron {payasosVendidos} Payasos donde su peso es de {totalPesoPayasos} kg

# y

# Se vendieron {munecasVendidas} Payasos donde su peso es de {totalPesoMuneca} kg


# """)


# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# saldo = float(input("Ingresa el saldo de tu cuenta de ahorro: "))
# interesAnual = 4
# balanceFinal = (interesAnual * 100 / saldo) + saldo
# segundoFinal = (((interesAnual * 100)*2) / balanceFinal) + balanceFinal
# terceroFinal = (((interesAnual * 100)*2) / segundoFinal) + segundoFinal
# print(f"""

# El balance final del primero anho es {balanceFinal}

# El balance final del segundo anho es {segundoFinal}

# El balance final del tercer anho es {terceroFinal}


# """)

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

# valorPan = 3.49
# descuentoPorcentaje = 60
# panDuro = 10
# costefinal = (((100-descuentoPorcentaje) * valorPan) / 100) * panDuro

# print(f"""
# Hoy se han vendido {panDuro} panes duros,
# donde el valor de una barra de pan fresco es de ${valorPan},
# se le aplica un descuento del {descuentoPorcentaje}.
# El coste final del pan duro vendido es {costefinal}


# """)
