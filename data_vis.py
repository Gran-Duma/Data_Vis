#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time

# import instrument ?
class Animate:

    def __init__(self,y_name,units):
        self.fig = plt.figure()
        self.y_name = y_name
        self.units = units
        self.col_1_name = 'Time'
        self.col_2_name = f'{self.y_name}'
        self.df = pd.DataFrame(columns=[self.col_1_name,self.col_2_name])
        self.ax = plt.gca()
        
    def Plot(self,i):
  
        # get time or query intstrument
        col_1 = (dt.datetime.now().strftime('%H:%M:%S.%f'))
        col_2 = eval(f'{self.y_name}_Reading()')

        # append end of dataframe
  
        self.df.loc[len(self.df.index)] = [col_1,col_2]


        # only show last entries of dataframe to avoid clutter
        self.df1 = self.df.tail(7)

        plt.cla()
        self.df1.plot(kind='line',x=self.col_1_name,y=self.col_2_name, color='red', ax=self.ax)



        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title(f'{self.y_name} over Time')
        plt.ylabel(f'{self.y_name} ({self.units})')

    def Animation(self):
        self.ani = animation.FuncAnimation(self.fig,self.Plot,interval=1000)
        plt.show()

def Temperature_Reading():

    temp = random.randint(1,10)

    # temp = instrument.GetTemp() ?

    return temp

def Resistance_Reading():

    res = random.randint(50,125)

    return res

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
    Temp_Graph = Animate('Temperature','C')
    Temp_Graph.Animation()

def Res_V_Time():
    global Res_Graph
    Res_Graph = Animate('Resistance','mOhm')
    Res_Graph.Animation()

if __name__ == '__main__':
    # Temp_V_Time()
    Res_V_Time()