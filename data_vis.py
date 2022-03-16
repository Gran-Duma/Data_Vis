# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:37:34 2022

@author: Brandon
"""

#!/usr/bin/env python3

from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import data_gen

# def ani():

#     FuncAnimation(plt.gcf(), animate, interval=1000)

#     plt.show()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='y1')
    plt.plot(x, y2, label='y2')

    plt.legend(loc='upper left')
    plt.tight_layout()

if __name__ == '__main__':

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    t1 = threading.Thread(target=ani)
    t2 = threading.Thread(target=data_gen.gen)

    t1.start()
    t2.start()

    plt.show()
