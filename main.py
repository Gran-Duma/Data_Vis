import gui_control as gc
import data_vis as dv

if __name__ == '__main__':

    # creates class instance and passes it to GUI
    reality = dv.Animate('K','mOhm')
    gc.run_gui(reality)