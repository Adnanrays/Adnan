

import constructor
from constructor import *
p=Person()

p.setName("Adnan")
p.setDob("20-12-2000")
p.setaddress("indore")
p.setAvgage(25)

print(p.getName(),"\t",p.getDob(),"\t",p.getAddress(),"\t",p.getAvgage())
print("name = ",Person.__name__)
print("module = ",Person.__module__)
print("bases = ",Person.__bases__)
print("dict = ",Person.__dict__)
print(p)


