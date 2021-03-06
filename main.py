# y = 2a* e^(x+4) + 5
import csv
import math
import random

X_MAX_VALUES = 10000
Y_POINTS_COUNT = 10

set_x = lambda: [float(int(i) / X_MAX_VALUES) for i in range(1, X_MAX_VALUES+1)]
func = lambda x: 2*math.e**(x+4) + 5
set_delta = lambda y_arrays:((y_arrays[1] - y_arrays[0])) * X_MAX_VALUES

def set_y(x_arrays):
    y = []
    for x in x_arrays:
        y.append(func(x))
    return y

def set_randon_y(y_arrays, delta):
    y_line = []
    for y in y_arrays:
        y_random_array = []
        for _ in range(0, Y_POINTS_COUNT):
            min_y = y - delta
            max_y = y + delta
            y_random = (random.uniform(min_y, max_y) * X_MAX_VALUES)
            y_random_array.append(y_random)
        y_line.append(y_random_array)
    return y_line


def write_to_csv_file(x_array, y_array):
    title = ['X', 'Y']
    with open('data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(title)
        for i in range(len(x_array)):
            for j in range(len(y_array[0])):
                data = f'{int(x_array[i] * X_MAX_VALUES)}, {int(y_array[i][j] * X_MAX_VALUES)}'

                filewriter.writerow(data.split(','))



def main():
    y_arr = set_y(set_x())
    delta = set_delta(y_arr)
    y = set_randon_y(y_arr, delta)
    write_to_csv_file(set_x(), y)


if __name__ == '__main__':
    main()
