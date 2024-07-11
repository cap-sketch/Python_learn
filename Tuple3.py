######tuple#######
tup1=("phy","chem","maths")
#Creation of python tuple without the use of parenthesis
#    is known as tuple packing.
tup2="a","b","c","d"     #can also be written like this
tup3=()
print(tup3,type(tup3))
print(type(tup2))
print(tup1)

tup4=(5,)   #one comma is compulsory for one element tuple
print(type(tup4))

#access elements
tup1=("hey",1,2,3,"boy")
print(tup1[0])
#slicing
print(tup1[1:4])
#deleting
del tup1