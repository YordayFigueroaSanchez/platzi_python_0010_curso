def find_volumen(length=1, width=1, height=1):
    return length * width * height

def find_area(length, width):
    return length * width

print(find_volumen(10, 20, 30))
print(find_area(10, 20))
print(find_volumen())
print(find_volumen(width=10))

def retornar_multiples_valores():
    return 1, 2, 3

a, b, c = retornar_multiples_valores()
print(a, b, c)


