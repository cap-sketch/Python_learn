#Attributes---class.attr
#          ---obj.attr(using self)

class student:
    school="RMS" #class attribute stored only one time in memory.
    def __init__(self,name,age):
        self.name=name
        self.age=age   #object attribute

s1=student("anmol",15)
print(s1.school)      
print(s1.name)  

