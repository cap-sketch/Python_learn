#inheritance
class car:
    color="black"
   
    def start(self):
        print("it starts the car")
    
    @staticmethod    
    def stop(self):
        print("it stops the car")

class ToyotaCar(car):
    def __init__(self,name):
        self.name=name           


car1=ToyotaCar("fortuner")
print(car1.name)
print(car1.color)        
car1.start()