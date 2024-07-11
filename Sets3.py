######sets#####
"""set is an unordered collection of data items which
   does not contain duplicate items.
   set element is unique adn must be immutable.
   however,set itself is mutable."""

#empty set
set1=set()
print(set1,type(set1))

#access items(indexing not allowed)
set1={1,2,3,4,5}
for i in set1:
    print(i)
#adding items
set1.add(7) 
set1.update({8,9,10})
print(set1)
#remove items
set1.remove(3) #key error comes if element doesn't exist
set1.discard(15) #without key error
print(set1)