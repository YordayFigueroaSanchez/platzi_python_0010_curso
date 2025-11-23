# Funciones lambda y fábrica de funciones

# Funciones lambda
f_lambda = lambda x: x + 1
print(f_lambda(1))

# funcion lambda con dos argumentos
f_lambda_dos = lambda x, y: x + y
print(f_lambda_dos(1, 2))

# funcion lambda con tres argumentos
f_lambda_tres = lambda x, y, z: x + y + z
print(f_lambda_tres(1, 2, 3))

# funcion multiplicador
def mi_funcion(n):
    return lambda x: x * n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)
print(duplicador(2))
print(triplicador(3))

