#!/usr/bin/env python3

import tkinter as tk
import data_vis as dv
import main as main
import sys
import webbrowser


def run_gui(self):
    """main window with options"""

    root = tk.Tk()
    root.geometry("600x300")

    root.title('Instrument Monitor')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    button_1 = tk.Button(root, text ='Load Instructions', command=instruct)
    button_1.grid(row=0,column=0,sticky=tk.EW)

    button_2 = tk.Button(root, text ='Start Visuals', command=self.Visuals)
    button_2.grid(row=1,column=0,sticky=tk.EW)

    button_3 = tk.Button(root, text ='Save Data', command=self.save)
    button_3.grid(row=2,column=0,sticky=tk.EW)

    button_4 = tk.Button(root, text ='Close and Exit', command=lambda:[root.destroy(),self.stop_save(),dv.ani_close(),sys.exit(0)])
    button_4.grid(row=3,column=0,sticky=tk.EW)

    root.mainloop()


def instruct():

    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == '__main__':

    run_gui()

