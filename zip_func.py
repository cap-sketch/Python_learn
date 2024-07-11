#zip() function
"""The zip is an inbuilt function in python.
   It takes items in sequence from a number of collection
   to make a list of tuples,where each tuple contains one item from each collection."""

A=[1,2,3]
B="xyz"
res=list(zip(A,B))
print(res) #makes list of tuples with one element each from collections.

res2=tuple(zip(A,B))
print(res2) #tuple of tuples

#note-->If the sequence are not of the same length then
#       the result of zip() has length of the shorter sequence.

A="abcd"
B=[1,2]
res=list(zip(A,B))
print(res)


#The inverse zip(*) function
"""the * operator is used within the zip function.
   the * operator unpacks a sequence into positional arguments."""

A,B=zip(*res)
print(A)
print(B)