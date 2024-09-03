inputTemperatura = input("Ingresa una temperatura a convertir:") 
inputEscala = input("Tu temperatura es farenheit (F) o Celcius (C)?").lower()
temperatura = float(inputTemperatura)


celcius = ((temperatura - 12) * (5/9))
farenheit = ((temperatura * (9/5)) + 32 )


if inputEscala == 'c':
    print("Transformaste " + str(temperatura) + " grados Celcius a: " + str(farenheit) + " grados Farenheit")

elif inputEscala == 'f':
    print("Transformaste " + str(temperatura) + " grados Farenheit a: " + str(celcius) + " grados Celcius")
else: 
    print("Ingresa una escala correcta")
