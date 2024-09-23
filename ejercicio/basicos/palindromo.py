# En esta funcion se comprueba si una palabra es palindromo o no

def palindromo(texto):
    # Esta linea elimina los espacios en blanco de la izquierda y derecha
    texto = texto.strip(texto)
    # Esta linea returna True o False y se utiliza [::-1] para invertir el string.
    # Es “cortar” la cadena pero sin especificar inicio ni fin, solo especificando el step; de esta manera avanzamos de -1 en -1; invirtiendo la cadena.
    return texto == texto[::-1]


print(palindromo("amo la paloma"))
