import utils

print(utils.get_population())
print(utils.A)
print(utils.B)


data = [
    {
        'Country': 'Colombia',
        'Population': 1000
    },
    {
        'Country': 'Bolivia',
        'Population': 2000
    }
]

def run():
    country = input('Type a country: ')
    print(utils.population_by_country(data, country))

if __name__ == '__main__':
    run()
