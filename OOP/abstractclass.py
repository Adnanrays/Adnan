from abc import ABC,abstractmethod

class Polygon:
    def __init__(self,):
        pass
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("i have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("i have 5 sides")
t=Triangle()
t.noofsides()
p=Pentagon()
p.noofsides()