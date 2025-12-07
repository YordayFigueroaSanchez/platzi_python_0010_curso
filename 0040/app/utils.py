def get_population():
    keys = ('col', 'bol')
    values = {1000, 2000}
    return dict(zip(keys, values))

A = 'Hola'
B = 'Adios'

'''
[
    {
        'Country': 'Colombia',
        'Population': 1000
    }
]
'''
def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result