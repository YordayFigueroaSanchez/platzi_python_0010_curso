def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
print_info(name="Alice", age=30, city="New York")

# Example usage with different keyword arguments:
print_info(product="Laptop", price=999.99, stock=25)