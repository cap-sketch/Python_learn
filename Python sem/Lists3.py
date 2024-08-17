from filecmp import cmp

"""Basic list operations"""

list1=[1,2,3,4,5]
list2=["anmol",21,7.5]

#length
print(len(list1))

#concatenation
list3=list1+list2
print(list3)

#repetition
print(list3*2)

#membership
print(5 in list1)

#iteration
for i in list1:
    print(i)


"""some in-built functions and methods"""
#min and max value
print("max and min values: ")
print(max(list1))
print(min(list1))

#remove all elements from the list
print(list3)
list3.clear()
print(list3)

#shallow copy of the list
"""creates a new copy of list and changes made to one list does not affect the other."""
list1=[1,2,3,4,5]
list3=list1.copy()
list1[0]=0
print(list1)
print(list3)

#direct assignment
"""the list3 points to the same list as list1 and changes made to list1 are reflected in list3 as it is the same list with different pointers."""
print()
print(list1)
list3=list1
list1[0]=55
print(list3)
print()

#occurences of object
print(list1)
print(list1.count(2))

#lowest index of object
print(list1.index(55))

#reversing a list
print(list1)
list1.reverse()
print(list1)
print()

#sorting a list
print(list1)
list1.sort()
print(list1)