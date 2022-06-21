import threading
from threading import *
class Hi(Thread):
    def run(self):
     for i in range(15):
        print("Hi",i)
t1=Hi()
t1.start()
