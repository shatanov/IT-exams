import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(file: str):
    df = pd.read_csv(file)

    x = df['X']
    y1 = df['Y1']
    y2 = df['Y2']
    y3 = df['Y3']
    y4 = df['Y4']
    y5 = df['Y5']
    y6 = df['Y6']
    y7 = df['Y7']
    y8 = df['Y8']
    y9 = df['Y9']
    y10 = df['Y10']
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    ax.scatter(x, y1,
               c='r',
               s = 1)
    ax.scatter(x, y2,
               c='g',
               s = 1)
    ax.scatter(x, y3,
               c='c',
               s = 1)
    ax.scatter(x, y4,
               c='m',
               s = 1)
    ax.scatter(x, y5,
               c='y',
               s = 1)
    ax.scatter(x, y6,
               c='k',
               s = 1)
    ax.scatter(x, y7,
               c='w',
               s = 1)
    ax.scatter(x, y8,
               c='#ad09a3',
               s = 1)
    ax.scatter(x, y9,
               c='b',
               s = 1)
    ax.scatter(x, y10,
               c=[[0.1, 0.63, 0.55]],
               s = 1)
    ax.set_facecolor('black')

    fig.set_figwidth(100)  # ширина и
    fig.set_figheight(100)  # высота "Figure"

    plt.show()


def main():
    read_csv_file('data.csv')



if __name__ == '__main__':
    main()