import tkinter as tk
import data_vis as dv
import data_gen as dg
import threading
import sys

def run_gui():
    """main window with options"""

    root = tk.Tk()
    root.geometry("600x300")

    button_1 = tk.Button(root, text ='Kill Data Gen', command=dg.gen_stop)
    button_1.config(width=20, height=2, pady=5)

    button_2 = tk.Button(root, text ='Kill Plot', command=dv.ani_close)
    button_2.config(width=20, height=2, pady=5) 

    button_3 = tk.Button(root, text ='Kill all and Exit', command=lambda:[root.destroy,dg.gen_stop(),dv.ani_close(),print('bye'),sys.exit(0)])
    button_3.config(width=20, height=2, pady=5)

    button_4 = tk.Button(root, text ='Copy and Save Data', command=dg.save_data)
    button_4.config(width=20, height=2, pady=5)

    button_5 = tk.Button(root, text ='Start Data Gen', command=gen)
    button_5.config(width=20, height=2, pady=5)

    button_6 = tk.Button(root, text ='Start Data Animation', command=vis)
    button_6.config(width=20, height=2, pady=5)

    button_1.pack()
    button_2.pack()
    button_3.pack()
    button_4.pack()
    button_5.pack()
    button_6.pack()

    root.mainloop()

def vis():
    """uses multithreading to write to call data vis module"""

    t2 = threading.Thread(target=dv.data_vis)
    t2.start()

def gen():
    """multithread start data gen"""

    t3 = threading.Thread(target=dg.gen)
    t3.start()

if __name__ == '__main__':

    t1 = threading.Thread(target=run_gui)

    t1.start()