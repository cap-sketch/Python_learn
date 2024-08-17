#Data types
"""each value in python belongs to a specifc data type
   it determine the opeations possible and storage method of that value."""
#numbers-contain numeric values(int,float,complex 2+5j)
#boolean-subtype of numbers,has two constant values-True,False
#Sequences
"""sequences is an ordered collection of items,where items are indexed with integers.
   such as String,list,tuple."""
#string
"""group of characters
   characters can be alfabet,digit,space,special symbol
   repersented using single,double or triple(multiline) quotes"""
str1="hello"
str2='12@ hey'
str3='''heyy
        boy''' #multiline string
print(str2)
print(str3)
#Lists
"""list is a sequence of different data types sepereated by commas and enclosed using square braces."""
list1=[2,3,4.5,"hello"]
list1[0]=55
print(list1)
#tuple
tup=(1,2,3,4)
print(tup)
#sets
"""set is an unordered collection of items seperated by commas and enclosed using curly braces
   unlike list,it cannot have duplicate enteries.
   sets are mutable but the elements of sets are immutable."""
set1={1,2,"hello",5.0}
set1.add(44)
print(set1)
#None
"""special data type with single values used to signify absence of values"""
a=None
print(type(a))
#dictionary
dict1={"name":"anmol","class":2,4:7.0}
print(dict1["name"])
