dict_1 = {}
for i in range(1, 5):
    dict_1[i] = i * 2
print(dict_1)

dict_2 = {i: i * 2 for i in range(1, 5)}
print(dict_2)

# diccionario de paises y su poblacion
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {country: random.randint(1, 100) for country in countries}
print(population)

## de listas a diccionario
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages)))

new_dict = {name: age for name, age in zip(names, ages)}
print(new_dict)

