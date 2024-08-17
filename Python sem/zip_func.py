#zip() function
"""zip function is an inbuilt function in python
   it takes items in sequence from a number of collections to make a list of tuples,
     where each tuple contains one item from each collection."""

a=[1,2,3]
b="hello"
c=list(zip(a,b))
print(c)

#inverse zip function
a,b=zip(*c)
print(a,b)