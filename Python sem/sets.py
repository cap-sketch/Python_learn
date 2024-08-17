#set
"""set is an unordered collection of data items
   does not contain duplicate elements.
   every set element is unique and immutable.
   however,set itself is mutable.
   elements are enclosed inside pair of curly braces."""

#empty set
set1=set()
print(set1,type(set1))

set2={"hello",23,5,23}
#access items
"""cannot access items by referring to an index as sets are unordered data types.
   but you can loop through the set items using for loop"""
for i in set2:
    print(i)

#set elements are immutable whereas set are mutable(add or remove items from set).
    """add items"""
set2.add("boy")
set2.add(55)
print(set2)

"""update items(add more than one item)"""
set2.update(["orange","mango"])
print(set2)

#remove element (key error))
set2.remove("mango")
print(set2)

#discard element

set2.discard("hihi")
set2.discard("orange")
print(set2)

#removes all the elements
set1.clear()

set1=set2.copy()
