from thred6 import*
import threading
from threading import*

class Racing(Thread):
    account:Account
    name=""
    def __init__(self,account,name):
        super().__init__()
        self.account=account
        self.name=name
    def run(self):
        for i in range(1,6):
            self.account.deposite(100)
            print(self.name,self.account.get_balance())

acc=Account()
t1=Racing(acc,"Ram")
t2=Racing(acc,"shyam")
t1.start()
t2.start()