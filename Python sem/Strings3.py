"""String manipulation methods"""
str1="Hello Brother"

#convert the first character to captial
print(str1.capitalize())

#count the number of occurences of a substring
print(str1.count("o"))

#check if value ends with substring
print(str1.endswith("er"))

str1="HelloBrother"
#search string and return index
print(str1.find("ther"))

#search string and return index
print(str1.index("ther"))

#check if alphanumeric
print(str1.isalnum())

#check if alphabets only
print(str1.isalpha())

"""check if islower()
            isupper()
            isascii()
            isdigit()
            isspace()"""

#split method
"""split a string into list of substring
   take input as seperator-where to split(optional)
   default seperator whitespace"""

str1="hello boy"
n=str1.split()
print(n)
