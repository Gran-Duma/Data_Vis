#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pandas as pd
import time
import threading
import webbrowser
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk

# import instrument ?
class Animate:

    def __init__(self,col_1_units,col_2_units):

        # make two vertical subplots on a single figure
        self.fig,(self.ax1,self.ax2) = plt.subplots(2)

        self.col_0_name = 'Time'
        self.col_0_name = f'{self.col_0_name}'

        self.col_1_name = 'Temperature'
        self.col_1_units = col_1_units

        self.col_2_name = 'Resistance'
        self.col_2_units = col_2_units

        # iniatilize a pandas dataframe to store all instrument readings
        self.df = pd.DataFrame(columns=[self.col_0_name,self.col_1_name,self.col_2_name])
        
        self.today = dt.datetime.today()
        
        self.date = self.today.strftime("%m_%d_%y")

    def instruct(self):

        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def Plot(self,i):
        """Reads instruments, updates dataframe, and draws subplots"""
  
        # Query instrument and set timestamp
        col_0 = (dt.datetime.now().strftime('%H:%M:%S.%f'))
        col_1 = eval(f'{self.col_1_name}_Reading()')
        # Resistance is a function of Temp for this demonstration
        col_2 = eval(f'{self.col_2_name}_Reading(col_1)')

        # append end of dataframe with instrument readings
        self.df.loc[len(self.df.index)] = [col_0,col_1,col_2]

        # only show last entries of dataframe to avoid clutter
        self.df1 = self.df.tail(7)

        # clear plot to avoid plotting same stuff on top of eachother
        self.ax1.clear()

        self.ax1.set_title(f'{self.col_1_name} vs. {self.col_0_name}')
        self.ax1.set_xlabel(self.col_0_name)
        self.ax1.set_ylabel(f'{self.col_1_name} ({self.col_1_units})')
        self.df1.plot(x=self.col_0_name,y=self.col_1_name,ax=self.ax1,legend=False,color='red')
  
        # rotate previous and current iterated timestamp
        for label in self.ax1.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)

        # self.ax1.set_ylim([450, 550])

        self.ax2.clear()

        self.ax2.set_title(f'{self.col_2_name} vs. {self.col_1_name}')
        self.ax2.set_xlabel(self.col_1_name)
        self.ax2.set_ylabel(f'{self.col_2_name} ({self.col_2_units})')

        self.df1.plot(x=self.col_1_name,y=self.col_2_name,ax=self.ax2,legend=False)

        # self.ax2.set_ylim([350, 500])

        plt.tight_layout()


    def Animation(self,master):
        """starts animation loop by calling Plot method"""
        
    
        self.ani = animation.FuncAnimation(self.fig,self.Plot,interval=1000)

        # if no tk frame specified, run in native FuncAnimation GUI
        if master:

            canvas = FigureCanvasTkAgg(self.fig, master = master) 
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid(row=3,columnspan=3,sticky=tk.NSEW)

            # create the Frame to house toolbar
            toolbar_frame = tk.Frame(master=master)
            toolbar_frame.grid(row=4,columnspan=3)
            # create the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            # shows save_flag state by matching with buttons that start/stop saving
            self.label_11 = tk.Label(master)
            self.label_11.grid(column=2,row=0,rowspan=3,sticky=tk.NSEW)


        if master == None:

            plt.show()
        

    def ani_close():
        """close all figures"""

        plt.close('all')

    def save_prep(self):
        """Uses threading to call primary data saving function"""
        self.t1 = threading.Thread(target=self.save_data)
        self.t1.start()

    def save_data(self):
        """writes instance dataframe to csv until stopped"""
        self.save_flag = True
        self.label_11.config(background='green')
        count = 0
        while self.save_flag == True:

            # saves csv every 10 seconds
            self.df.to_csv(f'{self.date}_' + 'data.csv')
            time.sleep(10)

            count +=1
            self.label_11.config(text=f'Saved {count} times!')

            if self.save_flag == False:
                
                print('Stopped saving')
                self.label_11.config(background='red')
                break

    def stop_save(self):
        self.save_flag = False


def Temperature_Reading():
    
    temp = 500
    temp += random.randint(-10,10)
    
    # temp = instrument.GetTemp() ?

    return temp

def Resistance_Reading(temp):

    res = temp*.87
    return res
    
def ani_close():
    """close all matplotlib stuff"""

    plt.close('all')

if __name__ == '__main__':

    Graph = Animate('K','mOhm')
    Graph.Animation(None)
 
