#identity operators
"""_the operators are used to check wheather two objects
    are of same type of not & they share the same location 
    or not.
   _identity operators---'is' & 'is not' 
   _Always returns true or false as output"""

#note-check if memory location is same

a=5
c=a
b=6
print(a is b)
print(a is not b)
print(a is c)
print(id(a),id(c),id(b)) #gives memory location address

str1="hello"
str2="hello"
print(str1 is str2)

#only work for single values like int,float,strings
#does not work on collection as they have different memory location.
list1=[10,20,30]
list2=[10,20,30]
print(list1==list2)     #check values
print(list1 is list2)    #check memory location
print(id(list1),id(list2))