numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result_2 = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result_2)