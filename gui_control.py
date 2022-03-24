#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import data_vis as dv
import sys


def run_gui(instance):
    """main window with options"""

    root = tk.Tk()
    #getting screen width and height of display
    width = root.winfo_screenwidth() 
    height = root.winfo_screenheight()

    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))

    root.title('Instrument Monitor')

    tabControl = ttk.Notebook(root)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Tab 1')
    tabControl.add(tab2, text ='Tab 2')

    tabControl.pack(expand = 1, fill ="both")

    tab1.columnconfigure(0, weight=1)
    tab1.columnconfigure(1, weight=1)

    button_01 = tk.Button(tab1, text ='Load Instructions', command=instance.instruct)
    button_01.grid(row=0,column=0,sticky=tk.EW)

    button_02 = tk.Button(tab1, text ='Save Data', command=instance.save_prep)
    button_02.grid(row=2,column=0,sticky=tk.EW)

    button_03 = tk.Button(tab1, text ='Stop Saving', command=instance.stop_save)
    button_03.grid(row=3,column=0,sticky=tk.EW)
    
    button_04 = tk.Button(tab1, text ='Close and Exit', command=lambda:[root.destroy(),instance.stop_save(),dv.ani_close(),sys.exit(0)])
    button_04.grid(row=4,column=0,sticky=tk.EW)

    button_11 = tk.Button(tab2, text ='Start Visuals', command=lambda:[instance.Animation(tab2)])
    button_11.pack()

    root.mainloop()



if __name__ == '__main__':

    instance = 'test'
    run_gui(instance)

