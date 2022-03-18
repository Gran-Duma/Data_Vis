# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:39:56 2022

@author: Brandon
"""
#!/usr/bin/env python3

import csv
import random
import time

def gen():

    x_value = 0
    total_1 = 1000
    total_2 = 1000

    fieldnames = ["x_value", "total_1", "total_2"]


    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while True:

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
<<<<<<< Updated upstream
    
=======

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
    df = pd.read_csv('data.csv')
    df.to_csv(f'{d1}_' + 'data.csv')

>>>>>>> Stashed changes
if __name__ == '__main__':

    gen()
