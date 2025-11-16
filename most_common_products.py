from collections import Counter

def most_common_products(orders: list[str]) -> Counter:
    product_counter = Counter(orders)
    return product_counter.most_common()

orders = ["apple", "banana", "apple", "orange", "banana", "apple"]
common_products = most_common_products(orders)
for product, count in common_products:
    print(f"{product}: {count}")