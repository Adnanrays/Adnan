class Car:
    count=0
    def __init__(self,brand,model):
        self.brandname=brand
        self.model=model
        Car.count += 1
    

    def getbrandname(self):
        return self.brandname
    def getmodel(self):
        return self.model
