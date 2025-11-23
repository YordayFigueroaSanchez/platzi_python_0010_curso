# tuplas

tecnologias = ("python", "javascript", "java")
print(tecnologias)
print(type(tecnologias))

alimentos = ("arroz", "frijoles", "papa")
print(alimentos)
print(type(alimentos))


# desempaquetado de tupla
a, b, c = tecnologias
print(a)
print(b)
print(c)

# dos tuplas de nuemros y sumarlas
numeros1 = (1, 2, 3)
numeros2 = (4, 5, 6)
numeros = numeros1 + numeros2
print(numeros)

# recorrer la tupla numeros e imprimir cada numero
for numero in numeros:
    print(numero)   

# para modificar una tupla debemos convertirla en lista
numerosModificar = list(numeros)
numerosModificar.insert(0, 10)
print(numerosModificar)
numeros = tuple(numerosModificar)
print(numeros)
