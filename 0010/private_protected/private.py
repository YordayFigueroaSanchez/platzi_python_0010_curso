class PrivateClass:
    def __init__(self):
        self.__private_attribute = "This is a private attribute"

    def __private_method(self):
        return "This is a private method"
    
    def public_method(self):
        return self.__private_method()
    
private_instance = PrivateClass()
# Accessing private attribute and method using name mangling
print(private_instance.public_method())
# print(private_instance.__private_attribute)
