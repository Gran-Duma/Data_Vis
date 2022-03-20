#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time

class Animate:

    def __init__(self,y_name):
        self.fig = plt.figure()
        self.y_name = y_name
        self.x = []
        self.y = []

    def Plot(self,i):
        # Add x and y to lists
        self.x.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        self.y.append(data_gen())


        # make dataframe out of list?
        self.df = pd.DataFrame(data=self.y,columns=[f'{self.y_name}'])
        old_index = self.df.index.tolist() 
        self.df = self.df.rename(index=dict(zip(old_index, self.x)))


        # Limit x and y lists to 20 items
        self.x1 = self.x[-20:]
        self.y1 = self.y[-20:]

        # Draw x and y lists
        plt.cla()
        plt.plot(self.x1, self.y1)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Temperature over Time')
        plt.ylabel('Temperature (deg C)')
    
    def Animation(self):
        self.ani = animation.FuncAnimation(self.fig,self.Plot,interval=1000)
        plt.show()

def data_gen():
    """returns value to be plotted"""

    y = random.randint(1,10)

    # temp = tc.MeasureTemp(self.inst_T)

    return y

def save_stop():
    """stops saving"""

    global save_flag
    save_flag = False
    
def save_data():
    """repeatedly save currently appending dataframe to csv"""


    today = dt.datetime.today()
    d1 = today.strftime("%m_%d_%y")

    global save_flag
    save_flag = True
   
    while save_flag == True:

        
        Temp_Graph.df.to_csv(f'{d1}_' + 'data.csv')
        time.sleep(10)
        print('Saved')

        if save_flag == False:
            
            print('Stopped saving')
            break

def ani_close():
    """close all matplotlib stuff"""

    plt.close('all')

def Temp_V_Time():
    global Temp_Graph
    Temp_Graph = Animate('T')
    Temp_Graph.Animation()

if __name__ == '__main__':
    Temp_V_Time()