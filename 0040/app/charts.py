import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()

if __name__ == '__main__':
    # generate_bar_chart(["a","b","c"],[1,2,3])
    generate_pie_chart(["a","b","c"],[1,2,3])