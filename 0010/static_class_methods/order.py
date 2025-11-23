class Order:
    @staticmethod
    def sort_items(items):
        return sorted(items)
    
    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)

# Example usage
items = [5, 2, 9, 1, 63, 42, 7]
sorted_items = Order.sort_items(items)
print("Sorted items:", sorted_items)

amount = 100
tax_rate = 15
tax = Order.calculate_tax(amount, tax_rate)
print(f"Tax on {amount} at {tax_rate}%: {tax}")