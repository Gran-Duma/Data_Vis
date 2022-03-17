import tkinter as tk
import data_vis as dv
import data_gen as dg
import threading
import sys

def run_gui():

    root = tk.Tk()
    root.geometry("400x200")

    button_1 = tk.Button(root, text ='Start', command=vis)
    button_1.config(width=20, height=2)

    button_2 = tk.Button(root, text ='Kill Data Gen', command=dg.gen_stop)
    button_2.config(width=20, height=2)

    button_3 = tk.Button(root, text ='Kill Plot', command=dv.ani_close)
    button_3.config(width=20, height=2) 

    button_4 = tk.Button(root, text ='Exit', command=lambda:[root.destroy,print('bye'),sys.exit(0)])
    button_4.config(width=20, height=2) 

    button_1.pack()
    button_2.pack()
    button_3.pack()
    button_4.pack()
    root.mainloop()

def vis():

    t2 = threading.Thread(target=dv.data_vis)
    t3 = threading.Thread(target=dg.gen)

    t2.start()
    t3.start()

if __name__ == '__main__':
    
    t1 = threading.Thread(target=run_gui)

    t1.start()