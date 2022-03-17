#!/usr/bin/env python3

import csv
import random
import time

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

        if yoyo == False:

            print("Ayo we donezo")
            break


def gen_stop():
    global yoyo
    yoyo = False

if __name__ == '__main__':

    gen()
