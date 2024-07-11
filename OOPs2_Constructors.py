#constructor
"""all clases have a function called _init_()
   which is always executed when object is being intitiated.
   -it is done automatically(can also be done automatically)"""

class student:
    #constructor
    #self parameter is a reference to the current instance
    #    of the class, and is used to access variables that 
    #    belongs to the class.

    #default constructor
    def __init__(self):
        pass
    
    #parameterised constructor
    def __init__(self,fullname):
        print(self)
        print("creating new student in database")
        self.name=fullname

s1=student("anmol")
print(s1.name)
print(s1)    

s2=student("cheetah")
print(s2.name)