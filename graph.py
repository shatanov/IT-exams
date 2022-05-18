import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(file: str):
    df = pd.read_csv(file)

    x = df['X']
    y = df['Y']
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    ax.scatter(x, y,
               c='r',
               s = 1)
    ax.set_facecolor('black')

    fig.set_figwidth(100)  # ширина и
    fig.set_figheight(100)  # высота "Figure"

    plt.show()


def main():
    read_csv_file('data.csv')



if __name__ == '__main__':
    main()
