# bucles while

i = 1
while i <= 10:
    print(i)
    # salir en caso de que i sea 5
    if i == 5:
        break
    i += 1

# usar un continue
i = 0
while i < 10:
    i += 1
    # saltar el numero 5
    if i == 5:
        continue
    print(i)