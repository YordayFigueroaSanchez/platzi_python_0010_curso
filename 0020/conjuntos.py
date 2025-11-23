# conjuntos
frutas = {"manzana", "banana", "chirimoya"}
print(frutas)
print(type(frutas))

frutas = {"manzana", "banana", "chirimoya", "manzana"}
print(frutas)
print(type(frutas))
print(len(frutas))

# conjunto de diferentes tipos
diferentes = {"manzana", "banana", "chirimoya", "manzana", 1, 2, 3, True, False}
print(diferentes)
print(type(diferentes))
print(len(diferentes))

# elemento en el conjunto
print("manzana" in frutas)
print("pera" in frutas)

# agregar un elemento
frutas.add("pera")
print(frutas)

# agregar varios elementos
frutas.update(["uva", "melon"])
print(frutas)

# eliminar un elemento
frutas.remove("banana")
print(frutas)

# eliminar un elemento con discard
frutas.discard("chirimoya")
print(frutas)

# eliminar un elemento con pop
frutas.pop()
print(frutas)

# eliminar todos los elementos
frutas.clear()
print(frutas)

# operaciones entre conjuntos, crear dos conjuntos a y b
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# union
print("union", a.union(b))

# interseccion
print("interseccion", a.intersection(b))

# diferencia
print("diferencia", a.difference(b))

# diferencia simetrica
print("diferencia simetrica", a.symmetric_difference(b))

# subconjunto
print("subconjunto", a.issubset(b))

# superconjunto
print("superconjunto", a.issuperset(b))

# disjuntos
print("disjuntos", a.isdisjoint(b))

# copia
print("copia", a.copy())