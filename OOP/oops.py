class Account:

    def __init__(self,number,accountType,balance):
        self.number=number
        self.accountType=accountType
        self.balance=balance

    def getnumber(self):
        return self.number
    def getaccountType(self):
        return self.accountType
    def getbalance(self):
        return self.balance
