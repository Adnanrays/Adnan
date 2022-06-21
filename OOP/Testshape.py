import childclass
from childclass import*
p=Rectangle()
p.setLength(5)
p.setWidth(5)

print(p.area())

import parentcircleclass
from parentcircleclass import *
p=Circle()
p.setradius(12)
print(p.area())

import childclass2
from childclass2 import*
p=Triangle()
p.setBase(10)
p.setHight(20)
print(p.area())

