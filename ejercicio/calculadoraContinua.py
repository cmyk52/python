# debe solicitar un numero, indicar que operacion y solicitar un segundo numero : luego debe solicitar nuevamente la operacion

mensaje = """

Bienvenido a la calculadora Continua, debes ingresar un numero, luego seleccionar una operacion (sumar, restar, dividir, multiplicar), luego un segundo numero. 
El resultado de este sera operado por un nuevo operador que tu ingreses.
Para salir, debes escribir "Salir"

"""
print(mensaje)

# Se guardara resultado en una variable global, donde inicialmente sera n1 y luego se mantendra como resultado
resultado = ""

# Se inicia un bucle infinito
while True:

    # Se valida si resultado contiene un valor
    if not resultado:
        # Se solicita ingresar el primer numero que sera igual a resultado
        resultado = int(input("Ingresa un numero : "))
        # Se inicia segundo bucle que evalua la operacion y no saldra del bucle hasta usar salir
        while True:
            # Se solicitaoperacion
            operacion = input("Ingresa una operacion : ")
            if operacion.lower() == "salir":
                print("Haz salido de la calculadora")
                break
            # sumar
            elif operacion == "sumar":
                # Se solicita n2 el cual sera el numero a operar del valor del resultado
                n2 = int(input("Ingrese otro numero : "))
                resultado = resultado + n2
                print(resultado)

            # restar
            elif operacion == "restar":
                n2 = int(input("Ingrese otro numero : "))
                resultado = resultado - n2
                print(resultado)

            # multiplicar
            elif operacion == "multiplicar":
                n2 = int(input("Ingrese otro numero : "))
                resultado = resultado * n2
                print(resultado)

            # dividir
            elif operacion == "dividir":
                n2 = int(input("Ingrese otro numero : "))
                resultado = resultado / n2
                print(resultado)
    break
