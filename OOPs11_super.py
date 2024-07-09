#super (part of inheritance)
class car:
    def __init__(self,type):
        self.type=type

    color="black"
    def start(self):
        print("it starts the car")
        
    def stop(self):
        print("it stops the car")

class ToyotaCar(car):
    def __init__(self,name,type):
        super().__init__(type)   #calling constructor using super
        self.name=name           


car1=ToyotaCar("fortuner","electric")
print(car1.type)
print(car1.color)        
car1.start()