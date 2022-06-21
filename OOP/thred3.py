import threading


def hello(name):
    for i in range(15):
        print(name,i)
t3=threading.Thread(target=hello,args=('Ram',))
t4=threading.Thread(target=hello,args=('shyam',))
t3.start()
t4.start()