import tkinter as tk
import data_vis as dv
import sys
import threading
import datetime as dt

def run_gui():
    """main window with options"""

    root = tk.Tk()
    root.geometry("600x300")

    button_1 = tk.Button(root, text ='start', command=dv.ani_master)
    button_1.config(width=20, height=2)

    button_2 = tk.Button(root, text ='save', command=save)
    button_2.config(width=20, height=2)

    button_3 = tk.Button(root, text ='exit', command=lambda:[root.destroy(),dv.save_stop(),sys.exit(0)])
    button_3.config(width=20, height=2)

    button_1.pack()
    button_2.pack()
    button_3.pack()

    root.mainloop()

def save():

    t1 = threading.Thread(target=dv.save_data)

    t1.start()
  

if __name__ == '__main__':

    run_gui()

