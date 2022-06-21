class Person:
    def __init__(self):
        self.name=""
        self.dob=""
        self.address=""
        self.Avg_age=0
    def setName(self,name):
        self.name=name
    def setDob(self,dob):
        self.dob=dob
    def setaddress(self,address):
        self.address=address
    def setAvgage(self,Avg_age):
        self.Avg_age=Avg_age
    def getName(self):
        return self.name
    def getDob(self):
        return self.dob
    def getAddress(self):
        return self.address
    def getAvgage(self):
        return self.Avg_age

    def __str__(self):
        return"name=%s\naddress=%s\nDob=%s\nAvgage=%s "%(self.name,self.address,self.dob,self.Avg_age)

