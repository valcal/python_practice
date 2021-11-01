"""
Problem 1

COORDINATE MATH: Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
"""

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return "Lenght of a line defined by {} and {} is {}.".format(self.coor1, self.coor2, ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**(1/2))
    
    def slope(self):
        return "Slope of a line defined by {} and {} is {}.".format(self.coor1, self.coor2, (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))
        
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
li.distance()
li.slope()
