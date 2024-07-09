#del keyword
"""used to delete the object properties or object itself."""

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=student("Anmol",15)
print(s1.name)
del s1.name
print(s1.age)
del(s1)
print(s1.name)
