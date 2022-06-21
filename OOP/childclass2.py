import parentclass
from parentclass import*
class Triangle(Shape):
    def __init__(self):
        self.base=0
        self.hight=0
    def setBase(self,base):
        self.base=base
    def setHight(self,hight):
        self.hight=hight
    def getBase(self):
        return self.base
    def getHight(self):
        return self.hight
    def area(self):
        return 0.5*self.hight*self.base
