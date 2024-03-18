import random

class coin:
    def __init__(self, rare = False , clean = True,head = True ,**kwargs):  #kwargs stands for keyword arguements . and this kwargs is used here to accept and pack the keyword arguements passed from the data dictionary of the pound class to the parent class coin using the super .

        for key,value in kwargs.item():
            setattr(self,key,value)       #set attribute sets the value of all these in the brackets and assigned to the self ,key ,value that is if we talk about original value than self attribute assign self to self and key to the original value and value to the value
            
            self.israre = rare
        self.isclean = clean
        self.heads = heads

        if self.israre:
            self.value = self.originalvalue * 1.25
        else:
            self.value = self.originalvalue

        if self.isclean:
            self.colour = self.cleancolour
        else:
            self.colour = self.rustycolour

        def rust(self):
            self.colour = self.rustycolour

        def __del__(self):
            print("coin spent")

        def flip(self):
            headsoptions = [True,False]
            choice = random.choice(headsoptions)
            self.heads = choice


class pound(coin):     #inherited class that is pound class inherited from coin class
                        #parent class = coin   , inherited class = pound
    def __init__(self):
        data = {
            "originalvalue": 1.00,
            "cleancolour": "gold",
            "rustycolour": "greenish",
            "numedges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data)       #super is parent class . by this statement we are passing the unpacked data by usig ** . we are passing the data in the keyword form by unpacking it and passing it in the init function of the coin class


#in this way we can create class for each coin,and create class for as many coins as we want and carry forward the project as long as we want . just we need to do is to create a dictionary in another class of coin and passing the super function in that
        
    
