# y = 2a* e^(x+4) + 5
import csv
import math
import random

X_MAX_VALUES = 10000
Y_POINTS_COUNT = 10

set_x = lambda: [float(int(i) / X_MAX_VALUES) for i in range(1, X_MAX_VALUES+1)]
func = lambda x: 2*math.e**(x+4) + 5
set_delta = lambda y_arrays:(y_arrays[1] - y_arrays[0]) / 2

def set_y(x_arrays):
    y = []
    for x in x_arrays:
        y.append(func(x))
    return y

def set_randon_y(y_arrays, delta):
    y_line = []
    for y in y_arrays:
        y_random_array = []
        for _ in range(0, 10):
            min_y = y - delta
            max_y = y + delta
            y_random = random.uniform(min_y, max_y)
            y_random_array.append(y_random)
        y_line.append(y_random_array)
    return y_line


def write_to_csv_file(x_array, y_array):
    title = ['X', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']
    with open('data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(title)
        for i in range(len(x_array)):
            data = f'{x_array[i]}, {y_array[i][0]}, {y_array[i][1]}, {y_array[i][2]}, {y_array[i][3]}, {y_array[i][4]}' \
                   f', {y_array[i][5]}, {y_array[i][6]}, {y_array[i][7]}, {y_array[i][8]}, {y_array[i][9]}'

            filewriter.writerow(data.split(', '))



def main():
    y_arr = set_y(set_x())
    print(set_delta(y_arr))
    delta = set_delta(y_arr)
    y = set_randon_y(y_arr, delta)
    write_to_csv_file(set_x(), y)


if __name__ == '__main__':
    main()
