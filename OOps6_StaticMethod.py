#static methods
"""methods that don't use the self parameter
   work at class level
   """

class student:
    @staticmethod
    def hello():
        print("say hello")

s1=student()
s1.hello()        