"""
Problem 2

CYLINDER CALCULATOR: Fill in the class to calculate cylinder volume and surface area.

EXAMPLE OUTPUT
c = Cylinder(2,3)
"""

class Cylinder:
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (self.pi*(self.radius)**2)*self.height
    
    def surface_area(self):
        return 2*(self.pi*(self.radius**2)) + (2*self.pi*self.radius*self.height)
        
c = Cylinder(2,3)
c.volume()
c.surface_area()
