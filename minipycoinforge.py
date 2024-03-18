import random
class Pound:

    value = 1.00         #these are 6 states of our class
    colour = "gold"
    numedges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True
    

coin1 = Pound()   #these are objects of pound class

print(type(coin1))
print(coin1.value)
print(coin1.colour)
coin1.colour = "greenish"    #code to change colour of coin . and in the same way we can change any state of the class by using this code
print(coin1.colour)

coin2 = Pound()       #another object declared of pound class and in this way using same type of code , we can declare as many objects as we do want
print(coin2.colour)

coin1.value = 1.25      #code to change the value of the coin
print(coin1.value)

print(coin2.value)

#CLASS METHODS = class methods are used when we want our class to behave in a certain way

class Pound:         

    def __init__(self):       #constructor = declaration of a constructor having a parameter self
                              #self is used to refer to a specific instance of this class when we write the class code . for eg - if we made a object coin1 using this class ,than this self will be replaced by class1 , and in a similar way when we make another object like class2 using this class than for that object that self will be replaced by class2 and so on.

        self.value = 1.00         #these are 6 states of our class
        self.colour = "gold"
        self.numedges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
        
        
    
class Pound:         
                                           #init method which we used as a constructor to construct our classes states .
    def __init__(self,rare = False):       #constructor = declaration of a constructor having a parameter self. cinstructor can have more than one parameter like here we took another parameter as rare which is a boolean type telling us whether the coin is rare or not
                                           #1ST parameter for any constructor is self always
        self.rare = rare           #self is used to refer to a specific instance of this class when we write the class code . for eg - if we made a object coin1 using this class ,than this self will be replaced by class1 , and in a similar way when we make another object like class2 using this class than for that object that self will be replaced by class2 and so on.

        if self.rare:       
            self.value = 1.25
        else:
            self.value = 1.00

                                #these are 6 states of our class
        self.colour = "gold"
        self.numedges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    def __del__(self):                 #destructor is called using del and consetructor is called using init . destructor is automatically called when a python programme is complete.
        print("coin is destroyed or coin spent")
        
    def rust(self):               #rust class method to change the colour of coin
        self.colour = "greenish"

    def clean(self):          
        self.colour = "gold"

    def flip(self):                    #flip class method to toss the coin and change the heads and tails of the coin
        headsoptions = [True,False]
        choice=random.choice(headsoptions)
        self.heads = choice
        

coin3 = Pound(rare=True)
coin4 = Pound()

print(coin3.rare)
print(coin4.rare)

print(coin3.value)
print(coin4.value)
print(coin4.colour)
coin4.rust()           #now,coin4 gets rusted
print(coin4.colour)

coin4.flip()
print(coin4.heads)

coin4.flip()
print(coin4.heads)
   
coin4.flip()
print(coin4.heads)

coin4.flip()
print(coin4.heads)
