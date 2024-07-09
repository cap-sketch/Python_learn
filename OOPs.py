#class
"""class is a blueprint for creating objects."""
#object 
"""instance of class"""

#class
class student:
    name=""
    roll=0
    age=15

student()
{
    print("i am a constructor")
}
#object
s1=student()    #object created
s1.name="anmol"
s1.roll=25
print(s1.name,s1.roll,s1.age)

class car:
    color="blue"
    model="new"
    brand="mercedes"

car1=car()
print(car1.color,car1.brand,car1.model)