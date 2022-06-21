import pickle

list=['Adnan','khan','pathan','123']

f=open('objtest','wb')

pickle.dump(list,f)
f.close()