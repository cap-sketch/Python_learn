#methods
"""methods are the functions that belong to objects.
   class---collection of attributes(prop)and methods."""

class student:
    def __init__(self,n):
        self.name=n
        print("i am a constructor")

    def hello(self):    #self is compulsory
        print("beta say hello",self.name)

s1=student("anmol")
s1.hello()        