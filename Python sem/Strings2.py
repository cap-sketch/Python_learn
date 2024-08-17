str1="Hello brother"
#accessing characters
print(str1[0])
print(str1[-1])

"""Errors"""
# print(str1[4.5])   ->type error-only integers are allowed for indexing
# print(str1[a])     ->name error-value of a not defined
# print(str1[100])   ->index error-index is out of range
# print(str1[1]))    ->syntax error-extra closing parenthesis

"""string slicing"""
str2=str1[1:5]    
print(str2)

"""note--strings are immutable in nature so we cannot change it after it has been created.
         however,we can create a new string with the same name."""

str1="hey boy"     #creating new string with the same name
print(str1)
# str1[0]="i"      type error- str object does not support item assignment (immutable)


"""modifying characters of string"""
#method 1 (using list)
"""A character of string can be updated by first converting the string into list and making the required change
   and then convert it back to string.(it act as string is made mutable/changeable)"""
list1=list(str1)
print(list1)
list1[3]="y"
print(list1)
str1=str(list1)
print(str1)

#method 2 (string slicing)
str2=str1[0:3]+"y"+str1[4:]
print(str2)
print()


"""deleting the string"""
print(str2)
# del str2[1]  type error->item deletion not allowed
del str2
# print(str2)  name error->str2 not defined

"""string format"""
#using format method
str2="{a}{b}".format(a="hello",b="boy")
print(str2)
#using f-strings
a="hello"
b="boy"
str2=f"{a}{b}"
print(str2)

