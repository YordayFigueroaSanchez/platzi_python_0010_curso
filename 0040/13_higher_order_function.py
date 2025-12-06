def increment(x):
    return x + 1

increment_2 = lambda x: x + 1

def higher_order_function(x, func):
    return x + func(x)

higher_order_function_2 = lambda x, func: x + func(x)

print(higher_order_function(2, increment))

print(higher_order_function_2(2, increment_2))

print(higher_order_function_2(2, lambda x: x * 5))
