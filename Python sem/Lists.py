#list
"""list is a versatile mutable data structure that can hold ordered collection of items.
   list are defined using square braces and can contain elements of different data structure."""

#empty list
l1=[]
print(type(l1),l1)
#creating list with elements
fruits=["mango","grapes","banana"]
#list with mixed data type
intro=["anmol",21,45.6]

#accessing elements 
print(intro[0])
print(intro[1])

#list slicing
print(fruits[1:3])

#modifying a list(mutable in nature)
fruits[0]="litchi"
fruits[1]="papaya"
print(fruits)

#appending at the end of list
fruits.append("mango")
fruits.append("grapes")
print(fruits)

#extending with another list
fruits.extend(["pineapple","watermelon"])
print(fruits)

#length of list
print(len(fruits))

#check if item is in the list(returns true or false)
print("banana" in fruits)

#concatenating string
fruits=fruits+intro
print(fruits)
