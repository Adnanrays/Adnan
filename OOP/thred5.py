import threading
import time
from threading import*
def first_thread():
    print("hi are u deamon thread?")
    for i in range(10):
        time.sleep(2)
        print("yes i am a deamon thread",i)
def second_thread():
    print("are u non deamon?")
    for i in range(10):
        time.sleep(2)
        print("yes i am a non deamon thread",i)
t2=threading.Thread(target=first_thread,daemon=True)
t1=threading.Thread(target=second_thread)
t1.start()
time.sleep(3)
t2.start()