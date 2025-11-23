class Person:
    global_discount = 10  # Descuento global para todas las personas

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount

# Example usage
Person.update_global_discount(15)
print("Global discount updated to:", Person.global_discount)