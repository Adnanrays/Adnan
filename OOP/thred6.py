import time
import threading

class Account:
    balance=0
    def __init__(self):
        self.lock=threading.Lock()
    def get_balance(self):
        time.sleep(2)
        return self.balance
    def set_balance(self,amount):
        time.sleep(2)
        self.balance=amount
    def deposite(self,amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal+amount)
        self.lock.release()