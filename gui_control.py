#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import data_vis as dv
import sys


def run_gui(instance):
    """main window with options"""

    root = tk.Tk()
    # getting screen width and height of display
    width = root.winfo_screenwidth() 
    height = root.winfo_screenheight()

    # setting tkinter window size
    root.geometry("%dx%d" % (width, height))

    root.title('Instrument Monitor')

    # create tabs
    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    
    tab_control.add(tab1, text ='Tab 1')
    tab_control.add(tab2, text ='Tab 2')

    tab_control.pack(fill= 'both', expand=True)

    tab1.columnconfigure(0, weight = 1)

    tab1.rowconfigure(0, weight = 1)
    tab1.rowconfigure(1, weight = 1)

    tab2.columnconfigure((0,1,2), weight=1)
 
    tab2.rowconfigure(0, weight=1, uniform='row')
    tab2.rowconfigure(1, weight=1, uniform='row')
    tab2.rowconfigure(2, weight=1, uniform='row')
    tab2.rowconfigure(3, weight=9, uniform='row')
    tab2.rowconfigure(4, weight=1, uniform='row')
    
    button_01 = tk.Button(tab1, text ='Load Instructions', command=instance.instruct, background='sea green',font=('Helvatical bold',20))
    button_01.grid(row=0,columnspan=2,sticky=tk.NSEW)
    
    button_02 = tk.Button(tab1, text ='Close and Exit', command=lambda:[instance.stop_save(),root.destroy(),sys.exit(0)],background='grey70',font=('Helvatical bold',20))
    button_02.grid(row=1,columnspan=2,sticky=tk.NSEW)


    button_11 = tk.Button(tab2, text ='Start Visuals', command=lambda:[instance.ani_close(),instance.Animation(tab2)],font=('Helvatical bold',20))
    button_11.grid(row=0,columnspan=2,sticky=tk.NSEW)

    button_12 = tk.Button(tab2, text ='Save Data',background='green', command=lambda:[instance.start_save()],font=('Helvatical bold',20))
    button_12.grid(row=1,columnspan=2,sticky=tk.NSEW)

    button_13 = tk.Button(tab2, text ='Stop Saving',background='red', command=instance.stop_save,font=('Helvatical bold',20))
    button_13.grid(row=2,columnspan=2,sticky=tk.NSEW)

    root.mainloop()

