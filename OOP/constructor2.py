class person:
    count=0

    def __init__(self):
        self.name=""
        person.count+=1
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name