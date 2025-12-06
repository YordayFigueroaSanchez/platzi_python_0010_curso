import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

result = functools.reduce(lambda counter, item: counter if counter > item else item, numbers, 0)
print(result)