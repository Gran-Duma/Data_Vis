#!/usr/bin/env python3

import csv
import pandas as pd
import random
import time
from datetime import date

def gen():
    """creates and appends csv"""

    global yoyo
    yoyo = True


    x_value = 0
    total_1 = 1000
    total_2 = 1000

    fieldnames = ["x_value", "total_1", "total_2"]


    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while yoyo == True:

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2
            }

            csv_writer.writerow(info)
            print(x_value, total_1, total_2)

            x_value += 1
            total_1 = total_1 + random.randint(-6, 8)
            total_2 = total_2 + random.randint(-5, 6)

        time.sleep(1)
<<<<<<< HEAD
<<<<<<< Updated upstream
    
=======
=======
>>>>>>> gui_control

        if yoyo == False:

            print("Ayo we donezo")
            break


def gen_stop():
    """kills data gen"""
    global yoyo
    yoyo = False

def save_data():
    """stops data gen and makes a copy of current data gen csv"""
    today = date.today()
    d1 = today.strftime("%m_%d_%y")
<<<<<<< HEAD
    df = pd.read_csv('data.csv')
    df.to_csv(f'{d1}_' + 'data.csv')

>>>>>>> Stashed changes
=======
    gen_stop()
    df = pd.read_csv('data.csv')
    df.to_csv(f'{d1}_' + 'data.csv')

>>>>>>> gui_control
if __name__ == '__main__':

    gen()
