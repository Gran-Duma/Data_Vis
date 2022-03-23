import gui_control as gc
import data_vis as dv
import threading
import tkinter as tk
class Master:

    def Visuals(self):
        """create Animation class"""
        self.Graph = dv.Animate('K','mOhm')
        self.Graph.Animation()

    def save(self):
        """assign thread to call data saving function"""

        t1 = threading.Thread(target=self.Graph.save_data)
        t1.start()

    def stop_save(self):
        
        self.Graph.stop_save()

    def create_gui(self):
        gc.run_gui(self)

if __name__ == '__main__':

    test = Master()
    test.create_gui()