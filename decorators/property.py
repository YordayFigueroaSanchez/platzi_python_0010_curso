class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)
    
circle = Circle(5)
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.53981633974483
circle.radius = 10
print(circle.radius)  # Output: 10
print(circle.area)    # Output: 314.1592653589793