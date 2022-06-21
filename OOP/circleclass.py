import inheritenceshape
from inheritenceshape import*
class Circle(Shape):
    PI=3.14
    def __init__(self,r,c="",b=0):
        self.radius=r
        super(Circle,self).__init__(c,b)
    def area(self):
        return self.radius*self.radius*Circle.PI

c1 = Circle(2,'Red',5)
c2 = Circle(3,'blue')
c3= Circle(4)
print(c1.area())
