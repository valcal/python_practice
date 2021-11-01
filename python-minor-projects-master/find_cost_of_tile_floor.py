"""
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.
"""

import math

def calculate_floor_cost(w, h, p, c):
    packages_needed = math.ceil((w * h) / p)
    print("You need {} packages and total cost of tiles will be: {}$".format(packages_needed, packages_needed * c))
          
print("Welcome to tile cost calculator!")
print('Remember - in case of numbers with decimals, use "." instead of ",".')
print("")
w = float(input("Input floor width in meters:"))
h = float(input("Input floor heigth in meters:"))
p = float(input("Input number of square meters of tiles in one package:"))
c = float(input("Input tile package cost in $:"))
print("")
calculate_floor_cost(w, h, p, c)
