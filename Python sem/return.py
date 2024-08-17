#return statement
"""return statement is used to exit a function and return a value(values) to the caller.
   it return a specified value or returns None."""

#single value return
def sum(a,b):
    return a+b

print("sum is: ",sum(1,2))

#multivalue return

def func():
    name="hey"
    cl=4
    age=21
    return name,cl,age

n,c,a=func()
print(n,c,a)