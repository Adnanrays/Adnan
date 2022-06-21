import threading
from threading import*
def hello():
    for i in range(0,15):
        print('hello',i)
def hi():
    for i in range (0,15):
        print('Hi',i)
hello()
hi()

t1=threading.Thread(target=hello())
t2=threading.Thread(target=hi)
t1.start()
t2.start()