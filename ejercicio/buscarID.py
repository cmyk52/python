id = 10
for element in range(5):  # range() es un iterable, similar al map
    print(element)
    if element == id:
        print("Encontrado id:", id)
        break
else:
    print("No encontre la id", id)
