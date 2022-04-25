"""
Practical Python - 1.5 The Bouncing Ball

Auntiewhnor Kpolie
Date: 04/25/2022

A rubber ball is dropped from a 
height of 100 meters and each time 
it hits the ground, it bounces back up 
to 3/5 the height it fell. Write a program
that prints a table showing the 
height of the first 10 bounces.
"""

ballHeight = 100

for i in range(1, 11):
    ballHeight = ballHeight * 3 / 5  # get current ball height

    # prints each "bounce" and current height
    print(f"{i} {round(ballHeight, 4)}")
