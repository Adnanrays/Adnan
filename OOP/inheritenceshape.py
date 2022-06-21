class Shape:
    def __init__(self,c,b):
        self.color=c
        self.borderwidth=b
    def area (self):
        return 0
    def setcolor(self,c):
        self.color=c
    def getcolor(self):
        return self.color
    def getborderewidth(self):
        return self.borderwidth