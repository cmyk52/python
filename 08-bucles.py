array = ["Mi Piton", "My Java", "My PHP", "My JS", "My Ruby"]

# While

i = 0

while i <= 5:
    print(i)
    i = i + 1

while i < len(array): # Para acceder a todos los elementos de la lista, evaluamos < y no <= ya que generamos un error al momento de evaluar el valor de i, ya que i contaraun numero mas donde el elemento de la lista no existe.
    print(array[i])
    i = i + 1


# For
# Es mejor para iterar listas, ya que es mas facil de leer y necesita menos codigo.


for element in array:
    print(element)