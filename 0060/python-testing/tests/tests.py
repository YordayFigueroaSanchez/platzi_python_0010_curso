def calculate_total(items, discount=0):
    total = 0
    for item in items:
        total += item['price']
    return total - discount

def test_calculate_total_without_items():
    items = []
    assert calculate_total(items) == 0

def test_calculate_total_with_items():
    items = [
        {'name': 'item1', 'price': 10},
        {'name': 'item2', 'price': 20},
    ]
    assert calculate_total(items) == 30

def test_calculate_total_with_discount():
    items = [
        {'name': 'item1', 'price': 10},
        {'name': 'item2', 'price': 20},
    ]
    assert calculate_total(items, discount=10) == 20

if __name__ == '__main__':
    test_calculate_total_without_items()
    test_calculate_total_with_items()
    test_calculate_total_with_discount()
