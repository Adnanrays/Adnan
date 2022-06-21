class Myrouter:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def getbrand(self):
        return self.brand
    def getmodel(self):
        return self.model


class Newrouter(Myrouter):
    def __init__(self,brand,model):
        self.firstname=""
        self.lastname=""
        super(Newrouter,self).__init__(brand,model)

    def setfirstname(self,firstname):
        self.firstname=firstname
    def setlastname(self,lastname):
        self.lastname=lastname
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
a=Newrouter("ford","Mustang")
a.setfirstname("adnan")
a.setlastname("khan")
print(a.getfirstname())
print(a.getlastname())
print(a.brand)
print(a.model)


