#string

#creating strings
str1="hello"
str2='hell"o'
str3="""hello   
how u doing."""   #triple quotes for multiline string.
print(str1)
print(str2)
print(str3)

#accessing characters
print(str1[0])

#string slicing
print(str1[:3])

#string concatenation
print(str1+" "+str2)

#string methods

#string-removing leading and trailing whitespaces
str1="  Hello  "
print(str1)
print(str1.strip())

#converting to lowercase and uppercase
print(str1.lower())
print(str1.upper())

#sting formatting
name="anmol"
age=20
#using f-string method
format=f"my name is {name} and i am {age} years old"
print(format)
#using format method
format="my name is {} and i am {} years old".format(name,age)
print(format)

#len of string
l=len(name)
print(l)

#check substring
ques="where are you going"
print("are" in ques)

#repeat a sting
str="hello"*5
print(str)