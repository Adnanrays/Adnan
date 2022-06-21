import threading
from threading import*

def hello():
    for i in range (15):
        print('hello',i)
t1=threading.Thread(target=hello)
t1.start()