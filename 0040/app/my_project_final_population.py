from read_csv import read_csv_by_country, get_population_by_country
from charts import generate_bar_chart




if __name__ == '__main__':
    data = read_csv_by_country('0040/app/data.csv', 'Argentina')
    population = get_population_by_country(data)
    labels = list(population.keys())
    values = list(population.values())
    generate_bar_chart(labels, values)    
    
