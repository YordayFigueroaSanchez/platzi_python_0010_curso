numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

numbers_2 = [element * 2 for element in range(1, 11)]
print(numbers_2)

numbers_3 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_3)


