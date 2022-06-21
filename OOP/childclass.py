import parentclass
from parentclass import*
class Rectangle(Shape):
    def __init__(self):
        self.length=0
        self.width=0
    def setLength(self,length):
        self.length=length
    def setWidth(self,width):
        self.width=width
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def area(self):
        return self.length *self.width
