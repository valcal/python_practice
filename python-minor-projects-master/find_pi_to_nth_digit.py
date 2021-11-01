"""
Find PI to the Nth Digit: Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
"""
from math import pi
from mpmath import mp

while True:
    choice = int(input("To how many digits should i print PI? (Max = 10 000)"))
    if choice <= 10000: 
        mp.dps = choice
        print(mp.pi)
        break
    else:
        print("Type in correct number up to 10000.")
