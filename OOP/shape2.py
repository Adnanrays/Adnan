import shape1
from shape1 import*
class Rectangle(Shape):
    def __init__(self,length,Width):
        self.length=length
        self.Width=Width
    def getlength(self):
        return self.color
    def getWidth(self):
        return self.Width
    def area(self):
        return self.length*self.Width
class circle(Shape):
    def __init__(self,radius,color="",borderwidth=0):
        self.radius=radius
        super(circle, self).__init__(color,borderwidth)
    def getradius(self):
        return self.radius
    def area(self):
        return 3.14*self.radius*self.radius


