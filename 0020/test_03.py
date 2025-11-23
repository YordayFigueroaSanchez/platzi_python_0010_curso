# Si tienes una tupla con duplicados, ¿cómo se comporta al unirse con otra tupla?
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 5, 6, 7, 8)
tupla3 = tupla1 + tupla2
print(tupla3)

# Si agregas 'naranja' a un conjunto que ya contiene 'naranja', ¿qué ocurrirá?
conjunto = {"manzana", "banana", "naranja"}
conjunto.add("naranja")
print(conjunto)