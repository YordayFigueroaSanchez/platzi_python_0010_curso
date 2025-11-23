# Listas

frutas = ["manzana", "banana", "chirimoya"]
print(frutas)
print(type(frutas))
print(len(frutas))
print(frutas[0])
print(frutas[1])
print(frutas[2])

# Modificar un elemento de la lista
frutas[1] = "pera"
print(frutas)

# Agregar un elemento a la lista
frutas.append("durazno")
print(frutas)

# Eliminar un elemento de la lista
frutas.remove("chirimoya")
print(frutas)

# Ordenar una lista
frutas.sort()
print(frutas)

# Invertir una lista
frutas.reverse()
print(frutas)

# Copiar una lista
frutas2 = frutas.copy()
print(frutas2)

# Borrar una lista
frutas.clear()
print(frutas)

# Eliminar una lista
# del frutas

# lista de diferentes tipos
lista = [1, "hola", True, 3.1416]
print(lista)
print(lista[:2])

# chequear de manzana esta dentro de la lista de frutas
print("manzana" in frutas)

# lista de vehiculos
vehiculos = ["auto", "moto", "bicicleta"]

# append
vehiculos.append(" helicoptero")
print(vehiculos)

# insert
vehiculos.insert(1, "avion")
print(vehiculos)

# remove
vehiculos.remove("auto")
print(vehiculos)

# pop
vehiculos.pop()
print(vehiculos)

# index
print(vehiculos.index("moto"))

# count
print(vehiculos.count("moto"))

# sort
vehiculos.sort()
print(vehiculos)

# reverse
vehiculos.reverse()
print(vehiculos)

# copy
vehiculos2 = vehiculos.copy()
print(vehiculos2)

# clear
vehiculos.clear()
print(vehiculos)

# del
# del vehiculos


# unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# extend
lista1.extend(lista2)
print(lista1)

# repeat
lista1 = [1, 2, 3]
lista2 = lista1 * 3
print(lista2)