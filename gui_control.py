#!/usr/bin/env python3

import tkinter as tk
import data_vis as dv
import sys
import threading
import webbrowser


def run_gui():
    """main window with options"""

    root = tk.Tk()
    root.geometry("600x300")

    root.title('Instrument Monitor')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    button_1 = tk.Button(root, text ='Load Instructions', command=instruct)
    button_1.grid(row=0,column=0,sticky=tk.EW)

    button_2 = tk.Button(root, text ='Start Visuals', command=dv.Temp_V_Time)
    button_2.grid(row=1,column=0,sticky=tk.EW)

    button_3 = tk.Button(root, text ='Save Data', command=save)
    button_3.grid(row=2,column=0,sticky=tk.EW)

    button_4 = tk.Button(root, text ='Close and Exit', command=lambda:[root.destroy(),dv.save_stop(),dv.ani_close(),sys.exit(0)])
    button_4.grid(row=3,column=0,sticky=tk.EW)

    root.mainloop()


def save():
    """assign thread to call data saving function"""

    t1 = threading.Thread(target=dv.Temp_V_Time_Save)
    t1.start()

def instruct():

    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == '__main__':

    run_gui()

