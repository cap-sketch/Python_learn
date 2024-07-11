#static methods
"""methods that don't use the self parameter
   work at class level
   """

class student:
    @staticmethod  #decorators
    def hello():
        print("say hello")

s1=student()
s1.hello()        

"""Decorators allows us to wrap another function 
   in order to extend the behavior of the wrapped 
   function, without permanently modifiying it."""