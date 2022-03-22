#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time

# import instrument ?
class Animate:

    def __init__(self,col_1_name,col_1_units):

        self.fig,self.ax1 = plt.subplots()

        self.col_0_name = 'Time'
        self.col_0_name = f'{self.col_0_name}'

        self.col_1_name = col_1_name
        self.col_1_units = col_1_units

        self.df = pd.DataFrame(columns=[self.col_0_name,self.col_1_name])
        
    def Plot(self,i):
  
        # get time or query intstrument
        col_0 = (dt.datetime.now().strftime('%H:%M:%S.%f'))
        col_1 = eval(f'{self.col_1_name}_Reading()')

        # append end of dataframe
  
        self.df.loc[len(self.df.index)] = [col_0,col_1]


        # only show last entries of dataframe to avoid clutter
        self.df1 = self.df.tail(7)

        # clear plot to avoid plotting same stuff on top of eachother
        plt.cla()

        self.ax1.set_title(f'{self.col_1_name} vs. {self.col_0_name}')
        self.ax1.set_xlabel(self.col_0_name)
        self.ax1.set_ylabel(f'{self.col_1_name} ({self.col_1_units})')


        self.df1.plot(x=self.col_0_name,y=self.col_1_name,ax=self.ax1)
        
        # needed due to appending nature of data
        for label in self.ax1.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)

        self.ax1.set_ylim([0, 273])

    def Animation(self):
        self.ani = animation.FuncAnimation(self.fig,self.Plot,interval=1000)
        plt.show()

    def save_data(self):
        
        # grabs current date 
        today = dt.datetime.today()
        date = today.strftime("%m_%d_%y")

        global save_flag
        save_flag = True
    
        while save_flag == True:

            # saves csv every 10 seconds
            self.df.to_csv(f'{date}_' + 'data.csv')
            time.sleep(10)
            print('Saved')

            if save_flag == False:
                
                print('Stopped saving')
                break

def Temperature_Reading():

    temp = random.randint(5,230)

    # temp = instrument.GetTemp() ?

    return temp

def Resistance_Reading():

    res = random.randint(50,125)

    return res

def save_stop():
    """stops saving"""

    global save_flag
    save_flag = False
    

def ani_close():
    """close all matplotlib stuff"""

    plt.close('all')

def Temp_V_Time():
    global Temp_Graph
    Temp_Graph = Animate('Temperature','K')
    Temp_Graph.Animation()

def Temp_V_Time_Save():
    Temp_Graph.save_data()

def Res_V_Time():
    global Res_Graph
    Res_Graph = Animate('Resistance','mOhm')
    Res_Graph.Animation()

if __name__ == '__main__':
    Temp_V_Time()
 