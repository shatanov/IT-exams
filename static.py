import statistics
import csv

variance = lambda data: statistics.pvariance(data)
mediana = lambda data: statistics.median([float(j) for i in data for j in data[i]])

def set_x_array(data: list):
    x = []
    for i in range(1, len(data)):
        x.append(data[i][0])
    return x

def set_y_array(data: list):
    y = []
    for i in range(1, len(data)):
        y.append(data[i][1:])
    return y


def mean_y(y: list):
    mean_y = []
    for i in range(len(y)):
        y_i = y[i]
        mean = statistics.mean([float(i) for i in y_i])
        mean_y.append(mean)
    return mean_y


def read_csv_file(file: str):
    with open(file, newline='') as f:
        data = csv.reader(f)
        return list(data)


def main():
    data = read_csv_file(file="data.csv")
    x = set_x_array(data=data)
    y = set_y_array(data=data)
    mean = mean_y(y=y)
    print(mediana(data=y))

if __name__ == "__main__":
    main()