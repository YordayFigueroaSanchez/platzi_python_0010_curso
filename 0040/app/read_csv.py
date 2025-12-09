import csv
import re

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def read_csv_by_country(path, country):
    data = read_csv(path)
    return list(filter(lambda item: item['Country/Territory'] == country, data))

'''
extraer los annos y su poblacion dado 
{'Rank': '33', 'CCA3': 'ARG', 'Country/Territory': 'Argentina', 'Capital': 'Buenos Aires', 'Continent': 'South America', '2022 Population': '45510318', '2020 Population': '45036032', '2015 Population': '43257065', '2010 Population': '41100123', '2000 Population': '37070774', '1990 Population': '32637657', '1980 Population': '28024803', '1970 Population': '23842803', 'Area (kmÂ²)': '2780400', 'Density (per kmÂ²)': '16.3683', 'Growth Rate': '1.0052', 'World Population Percentage': '0.57'}
'''
def get_population_by_country(data):
    print(data)
    patron = r'\b(\d{4})\s+(Population)\b'
    population = {}
    result = {clave[:4]: valor for clave, valor in data[0].items() if re.search(patron, clave)}
    return result

def get_world_percentages(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per

if __name__ == '__main__':
    data = read_csv_by_country('0040/app/data.csv', 'Argentina')
    print(get_population_by_country(data))
