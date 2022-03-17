#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def data_vis():
    """creates animation from current figure then shows it in new window"""

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()

def animate(i):
    """reads from csv and makes figure"""

    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='y1')
    plt.plot(x, y2, label='y2')

    plt.legend(loc='upper left')
    plt.tight_layout()

def ani_close():
    plt.close('all')

if __name__ == '__main__':

    data_vis()
