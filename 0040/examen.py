n = []
for i in range(1, 6):
    if i <= 2:
        n.append(i - 1)
print(n)

n = [i-1 for i in range(1, 6) if i <= 2]
print(n)

def suma(a, b):
    result = a + b
    print(result)
    return result

suma_set = {}

suma_set = suma(1, 2)
suma_set = suma(3, 4)

print(suma_set)

d = {}
for e in range(1,6):
    if e<=2:
        d[e] = e-1
print(d)

d = {e:e-1 for e in range(1,6) if e<=2}
print(d)