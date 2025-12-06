# diccionario de paises y su poblacion
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {country: random.randint(1, 100) for country in countries}
print(population)

result = {country: population for country, population in population.items() if population > 50}
print(result)

# obtener las vocales de texto 
texto = 'Hola, soy yorday'
vocals_count = {vocal: texto.count(vocal) for vocal in texto if vocal in 'aeiou'}
print(vocals_count)
vocals_unique = {vocal: vocal.upper() for vocal in texto if vocal in 'aeiou'}
print(vocals_unique)