#parameters
"""actual parameters are those parameters that are passed in function call(driver code)
   whereas formal parameters are those parameters that are passed in function defination(master code)
   formal parameters are called as arguments."""

"""arguments"""

#required arguments
"""required arguments are the arguments passed to a function in correct positional order.
   here,the number of arguments in the function call should match exactly with function defination."""

def sum(a,b):
    print("in req,sum is: ",a+b)
    return None
sum(5,6)

#default argument
"""default argument is an argument that assumes a default value if a value is not provied in the function call for that argument."""
def func(a=5,b=6):
    print("sum is: ",a+b)
    return None
func()
func(20,25)


#keyword argument
"""keyword argument is used to pass the values with name of the variable so that we can pass values without bothering about the sequence of parameters."""
def func(a,b):
    print("sum is: ",a+b)
    return None
func(b=5,a=6)

#variable length argument
"""var args is used to take arguments of different lengths."""
def sum(*a):
    s=0
    for i in a:
        s=s+i
    print("sum is:",s)

sum(1)
sum(1,2,3)
sum()