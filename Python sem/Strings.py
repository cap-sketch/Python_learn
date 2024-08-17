#String
"""string is a group of characters enclosed in single,double or triple quotes.
   string are immutable in nature means value cannot be changed after creation.
   characters of strings is encoded in ASCII character."""

#creating strings
str1="hello"
str2='helloboy'
str3='''hey
how u doing...'''
print(str1,str2,str3)

#accessing character of strings
str1="python"
print(str1[0])
print(str1[1])
print(str1[-1])    #last character of string using negative index

#string slicing
sub=str1[1:4]
print(sub)

#string concatenation
str2="Hello"
print(str2+" "+str1)

"""string methods"""
#removing leading and trailing whitespaces
str3="    hello  brother     "
print(str3)
print(str3.strip())

#converting to lowercase and uppercase
print(str2)
print(str2.lower())
print(str2.upper())

#finding substring(return -1 if not found)
index=str2.find("lo")
print(index)

#string fomatting
#using f-strings
str1="boy"
str2=f"hello {str1}"
print(str2)
str3="hello {}".format(str1)
print(str3)

#string length
str1="python"
print(len(str1))

#check if substring is present(returns true or false)
str1="helloboy"
print("boy" in str1)

#repeat a string
print("hello "*5)

#escape characters
str1="hello\nboy"
print(str1)