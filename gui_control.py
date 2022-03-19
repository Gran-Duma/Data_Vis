import tkinter as tk
import data_vis as dv
import sys

def run_gui():
    """main window with options"""

    root = tk.Tk()
    root.geometry("600x300")

    button_1 = tk.Button(root, text ='start', command=dv.ani_master)
    button_1.config(width=20, height=2)

    button_2 = tk.Button(root, text ='save', command=dv.save_data)
    button_2.config(width=20, height=2)

    button_3 = tk.Button(root, text ='exit', command=lambda:[dv.ani_close(),root.destroy(),sys.exit(0)])
    button_3.config(width=20, height=2)

    button_1.pack()
    button_2.pack()
    button_3.pack()

    root.mainloop()

if __name__ == '__main__':

    run_gui()
