#########string############
"""creating"""
str1='hello'
str2="hey"
str3="""hola,
amigo."""

print(str1)
print(str2)
print(str3)

#indexing allow negative address references to access 
#   characters from back of string.
print(str1[-1],str1[-2])

#string slicing can also be done using negative index
print(str1[-5:-1])

# str1[0]='h'   (not allowed)
# print(str1)  

str4="boy"  
# del str4[0]  type error
del str4     #string deleted
print(str4)

