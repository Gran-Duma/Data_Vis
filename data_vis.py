#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time

def ani_master():

    global s
    s = True

    fig = plt.figure()
    xs = []
    ys1 = []


    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys1), interval=1000)
    plt.show()

def data_gen():

    y = random.randint(1,10)

    return y

def save_stop():
    """stops saving"""
    global s
    s = False

def save_data():

    today = dt.datetime.today()
    d1 = today.strftime("%m_%d_%y")
   
    while s == True:
        df.to_csv(f'{d1}_' + 'data.csv')
        time.sleep(10)
        print('saved')

        if s == False:
            print('Stopped saving')
            break

def ani_close():
    
    plt.close('all')


# This function is called periodically from FuncAnimation
def animate(i, xs, ys1):

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys1.append(data_gen())

    # make dataframe out of list?
    global df
    df = pd.DataFrame(ys1)

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