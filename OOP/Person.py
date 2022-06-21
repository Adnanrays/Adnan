class person:
    count=0
    def __init__(self, name, address):
        self.firstname= name
        self.address = address
        person.count += 1

    def setfirstname(self,name):
        self.firstname=name

    def getfirstname(self):
        return self.firstname

    def getAddress(self):
        return self.address