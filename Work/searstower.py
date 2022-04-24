"""
Practical Python - 1.2 Sears Tower vs Dollar Bills

by Auntiewhnor Kpolie
Date: 04/25/2022

Problem: One morning, you go out and place a dollar bill 
on the sidewalk by the Sears tower in Chicago. 
Each day thereafter, you go out and double the number of bills. 
How long does it take for the stack of bills
to exceed the height of the tower?
"""

# Variables:
# Day: what day it is (day = 1)
# Bill thickness: how thick a dollar bill is (0.0043 in or 0.11 mm)
# The number of bills (Doubles each day)
# Height of Sears tower (1450 ft, 442.1 meters)

# unit I'll use: meters

# Quick Math
# height of bill stack = Bill thickness * number of bills

from tracemalloc import start


searsTowerHeight = 442.1  # meters
bill_thickness = 0.11 * 0.001  # thickness in meters
day = 1
bill_number = 1
billStackHeight = bill_thickness * bill_number

while billStackHeight < searsTowerHeight:
    print(f"{day} {bill_number:,} {billStackHeight}")
    day += 1
    bill_number *= 2
    billStackHeight = bill_thickness * bill_number

print(
    f"\nTotal days: {day} \
    \nNumber of bills: {bill_number:,} \
    \nHeight of bill stack: {billStackHeight}"
)

