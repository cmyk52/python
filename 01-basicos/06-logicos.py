edad = 22

# AND: En este caso realiza 2 validacion, primero si es mayor a 20 y segundo si es menor de 30, en caso de que ambos den True, el resultado de la evaluacion final sera True, en caso de que el primero de False, no se ejecuta lo siguiente del codigo y dara como resultado final False.
# Si el primero da True y el segundo False, se ejecutara el codigo hasta que de False
print(edad > 20 and edad < 30)

# OR: Evalua ambos casos, si alguno da True el resultado sera True

print(edad < 20 or edad < 30)

# NOT: Negara lo que evaluemos, quiere decir que si usamos not True, el resultado sera False
print(not True)
# Para el caso evaluaremos que edad sea mayor a 17, como estamos negando la evaluacion True, dara como resultado False. *not ejecutara todo lo que era dentro de las parentesis.
print(not (edad > 17))

####
# IF: Realiza la evaluacion hasta que da como resultado True, el resto del codigo no se ejecuta
puntaje = 13

if puntaje >= 95:
    print("Aprobado con honores")

elif puntaje >= 50:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")

print("Fuera del IF")

####
# TERNARIOS: Cambia como utilizamos if y else, dovolviendo un valor que almacenaremos en variables

mensaje = "Es Mayor" if edad > 18 else "Es Menor"
print(mensaje)
