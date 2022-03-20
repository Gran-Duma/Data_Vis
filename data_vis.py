#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time

def ani_master():
    """primary data vis coordinating function"""

    fig = plt.figure()
    xs = []
    ys1 = []


    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys1), interval=1000)
    plt.show()

def data_gen():
    """returns value to be plotted"""

    y = random.randint(1,10)

    return y

def save_stop():
    """stops saving"""

    global s
    s = False

def save_data():
    """repeatedly save currently appending dataframe to csv"""

    today = dt.datetime.today()
    d1 = today.strftime("%m_%d_%y")

    global s
    s = True
   
    while s == True:

        df.to_csv(f'{d1}_' + 'data.csv')
        time.sleep(10)
        print('Saved')

        if s == False:
            
            print('Stopped saving')
            break

def ani_close():
    """close all matplotlib stuff"""

    plt.close('all')



def animate(i, xs, ys1):
    """iterated plot function called by FuncAnimation according to interval"""

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys1.append(data_gen())

    # make dataframe out of list?
    global df
    df = pd.DataFrame(data = ys1, columns=['T'])
    old_index = df.index.tolist()
    df = df.rename(index=dict(zip(old_index, xs)))


    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys2 = ys1[-20:]

    # Draw x and y lists
    plt.cla()
    plt.plot(xs, ys2)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')

if __name__ == '__main__':

    ani_master()
