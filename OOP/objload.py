import pickle

import objser
file=open('objtest','rb')
file1=open('objtest1','w')

newone = pickle.load(file)

for i in newone:
    file1.write(" "+i)
file.close()