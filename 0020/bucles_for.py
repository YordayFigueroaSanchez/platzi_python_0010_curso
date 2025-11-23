# bucles for

palabra = "Python"
for letra in palabra:
    print(letra)    

frutas = ["manzana", "banana", "chirimoya"]
for fruta in frutas:
    print(fruta)


# usar la intruccion break en un for
for i in range(5):
    print(i)
    if i == 3:
        break

# usar la intruccion continue en un for
for i in range(5):
    if i == 3:
        continue
    print(i)


# usar un rango de numero del 12 al 45
for i in range(12, 45):
    print(i)

# usar un rango de numero del 12 al 45 con un salto de 5
for i in range(12, 45, 5):
    print(i)

# usar un rango de numero del 12 al 45 con un salto de 5 y un rango negativo
for i in range(45, 12, -5):
    print(i)

