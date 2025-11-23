def add(a,b,c):
    return a + b + c

# Example usage:
numbers = (1, 2, 3)
result = add(*numbers)
print(f"Sum: {result}")

def show_details(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Example usage:
person_info = {"name": "Alice", "age": 30, "city": "New York"}
show_details(**person_info)