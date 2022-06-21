class Automobile:

    def __init__(self):
        self.color=""
        self.speed=0
        self.make=""
        self.noofgears=4

    def setcolor(self,color):
        self.color=color

    def getcolor(self):
        return self.color

    def setspeed(self,speed):
        self.speed=speed

    def getspeed(self):
        return self.speed

    def setmake(self,make):
        self.make=make

    def getmake(self):
        return self.make

    def getnoofgears(self):
        return self.noofgears


    def Break(self):
        if self.noofgears>5:
            print("break")
        else:
            print("continue")
a=Automobile()
a.Break()
a.setcolor("red")
print(a.getcolor())
a.setspeed(90)
print(a.getspeed())






