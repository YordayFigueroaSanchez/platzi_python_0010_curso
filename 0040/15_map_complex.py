items = [
    {
        'product': 'shirt',
        'price': 100
    },
    {
        'product': 'pants',
        'price': 200
    },
    {
        'product': 'shoes',
        'price': 300
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

