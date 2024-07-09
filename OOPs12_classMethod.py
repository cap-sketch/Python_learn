#class method
"""class method is bound to the class and recieves the class 
   as an implicit first argument"""

class person:
    name="anonymous"
    @classmethod
    def changename(self,name):
        self.name=name


p1=person()
p1.changename("anmol")
print(p1.name) 

print(person.name)