def sum(*args):
    total = 0
    for number in args:
        total += number
    return total

# Example usage:
result = sum(1, 2, 3, 4, 5)
print(f"Sum: {result}")

# Example usage with different number of arguments:
result = sum(10, 20)
print(f"Sum: {result}")