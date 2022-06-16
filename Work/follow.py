"""
Practical Python - Generators

Author: Auntiewhnor Kpolie
Created: 06/16/2022

stocklog.csv is a continuous stream of data
which comes from running stocksim.py
in the Data folder.

This program reads stocklog.csv and
prints out stocks with change less than 0.
"""
import os
import time

f = open('Data/stocklog.csv')
f.seek(0, os.SEEK_END)  # move pointer to the end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)  # stop for 0.1 seconds, then try again
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
