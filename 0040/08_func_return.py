def sum_range(max):
    sum = 0
    for i in range(max):
        sum += i
    return sum

def sum_range_2(min, max):
    sum = 0
    for i in range(min, max):
        sum += i
    return sum

print(sum_range(10))
print(sum_range(100))
print(sum_range_2(10, 100))