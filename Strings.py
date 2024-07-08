#string is a sequence of characters
#string can be initialised using singl,double(preffered),triple braces.
str1="this is a string"
str2='this is also a string'
str3="""this is another string"""

str4="this a string.\nwe are creating in \tpython"
print(str4)

#operations on stings
#concatenation
str1="anmol"
str2="pratap"
str3=str1+" "+str2
print(str3)

#string length
l=len(str3)
print(l)

#indexing of string(0,1,2,3,....)
print(str3[0])
print(str3[1])
print(str3[2])
print(str3[3])
print(str3[4])
#str[3]='a'   Not allowed(we can access characters using index but not manipulate.)

#slicing--accessing parts of string
#     str[starting index:ending index]
print(str3[3:])
print(str3[:4])
print(str3[3:8])    #8 not included

#slicing using negative index (......,-3,-2,-1)
print(str3[-6:-1])
