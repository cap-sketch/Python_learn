#sets--set is the collection of the unordered items(not indexing ).
#    --each element in the set must be unique and immutable.

#set can store boolean,int, float,str,tuple as they are immutable.
#but it cannot store list or dictionary as they are mutable.

#duplicate values not allowed.(ignored)

#sets are mutable--add or remove elements.
#elements of sets are immutable--cannot be modified.

num={1,2,3,4,5,"hello",6,96.5}
print(num)
print(type(num))
print(len(num))

num2=set() #emtpy set
print(type(num2))

#set methods

num2.add("hey") 
num2.add(1)

num2.remove(1)

print(num2)

num2.clear()
print(len(num))

#remove an element in random order
print(num)
num.pop()
num.pop()
print(num)