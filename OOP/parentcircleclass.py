import parentclass
from parentclass import*
class Circle(Shape):
    def __init__(self):
        self.radius=0
    def setradius(self,radius):
        self.radius=radius
    def getradius(self):
        return self.radius
    def area(self):
        return 3.14*self.radius*self.radius

