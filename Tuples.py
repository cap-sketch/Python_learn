#Tuple-A builtin data type that lets us create immutable sequence of values.

tup=(84,34,25,14,"hello")
print(tup)
print(type(tup))
print(tup[0])

# tup[0]=45--not allowed as tuple are immutable.

tup1=(4,)   #comma is important with single value
print(type(tup1))  

#tuple slicing
print(tup[0:2])

#index method-return index of first occurence
print(tup.index(25))

#count method--return number of occurnces
print(tup.count(14))