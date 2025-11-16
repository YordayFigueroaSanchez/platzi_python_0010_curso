class BaseClass:
    def __init__(self):
        self._protected_attribute = "This is a protected attribute"

    def _protected_method(self):
        return "This is a protected method"
    
base = BaseClass()
print(base._protected_attribute)  # Accessing protected attribute
print(base._protected_method())  # Accessing protected method