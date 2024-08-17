#functions
"""functions are used to organise the code into logical blocks and perform some action.
   empasises on code reusablity.
   master code-function def
   driver code-function call"""

#syntax
"""starts with def keyword
   def function_name(parameters):
     doc string
     function body
     return value"""

#function to square the given number
def square(a):              # a is formal parameter or argument
    print("squaring the number...")
    return a*a

n=int(input("enter any number: "))
sqr=square(n)          # n is actual parameter
print("the squarer of given number is: ",sqr)

