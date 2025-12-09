from read_csv import read_csv, get_world_percentages
from charts import generate_pie_chart

if __name__ == '__main__':
    data = read_csv('0040/app/data.csv')
    names, per = get_world_percentages(data)
    generate_pie_chart(names, per)