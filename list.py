#######List#######
"""list is a versatile,mutable data structure in python
   that can hold an ordered collection of items.
   --lists are defined using square braces[] and
     can containg elements of different data types."""

"""creating list"""
#empty list
list1=[]
print(list1)

#list with elements
list1=["apple","mange","banana"]
print(list1)

#list with mixed data
list1=[1,"two",3.0,True]
print(list1)


"""access elements"""
#accessing individual elements 
print(list1[0])

#slicing a portion of list
print(list1[1:3])


"""modifying list"""
#modifying an element
list1[0]="cheetah"
print(list1)

#appending to end of list
list1.append("hey")
print(list1)

#extending with another list
list2=[1,2,3]
list1.extend(list2)
print(list1)
list1.extend(["heyboy","howudoing"])
print(list1)

"""list operations"""
#length of list
print(len(list1))

#check if an item is item is in list
print(2 in list1)

#concatenating lists
list1=[1,2,3]
list2=[4,5]
combined=list1+list2
print(combined)

