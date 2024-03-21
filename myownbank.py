class account:
    def __init__(self,name,balance,minbalance):
        self.name = name
        self.balance = balance
        self.minbalance = minbalance

    def deposit(self,amount):
        self.balance += amount  #this notation is similar to self.balance = self.balance + amount

    def withdraw(self,amount):
        if self.balance - amount >= self.minbalance:
            self.balance -= amount   #this notation is simalar to self.balance = self.balance - amount

        else:
             print("sorry!! not enough funds !!")

    def statement(self):
        print("account balance:${}".format(self.balance))

class current(account):    #inherited class and the parent class is account . the whole data of the parent class is passed to the inherited class also . hence , the data of the parent class is accessible to the inherited class also
    def __init__(self,name,balance):
        super().__init__(name,balance,minbalance = -1000)  #passing its data to the super class which is always the parent class
        
    def __str__(self):
        return "{}'s current account : balance ${}".format(self.name,self.balance)
    
    
class savings(account):    
    def __init__(self,name,balance):
        super().__init__(name,balance,minbalance = 0) 
        
    def __str__(self):
        return "{}'s savings account : balance ${}".format(self.name,self.balance)
