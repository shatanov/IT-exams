import statistics
import csv
import numpy
import matplotlib.pyplot as plt

mean = lambda data: statistics.mean(data)
variance = lambda data: statistics.variance(data)
mediana = lambda data: statistics.median(data)
perc_25 = lambda data: numpy.percentile(data, 25)
perc_75 = lambda data: numpy.percentile(data, 75)
def set_x_array(data: list):
    x = []
    for i in range(1, len(data)):
        x.append(data[i][0])
    return x

def set_y_array(data: list):
    y = []
    for i in range(1, len(data)):
        y.append(int(data[i][1]))
    return y



def read_csv_file(file: str):
    with open(file, newline='') as f:
        data = csv.reader(f)
        return list(data)

def draw_graph(data):
    plt.hist(data, 20)
    plt.axvline(perc_25(data=data), color='r')
    plt.axvline(perc_75(data=data), color='b')
    plt.show()


def main():
    data = read_csv_file(file="data.csv")
    x = set_x_array(data=data)
    y = set_y_array(data=data)
    mean_y= mean(data=y)
    variance_y = variance(data=y)
    med = mediana(data=y)
    print(mean_y)
    print(variance_y)
    print(med)
    print(perc_25(data=y))
    print(perc_75(data=y))
    draw_graph(data=y)



if __name__ == "__main__":
    main()
