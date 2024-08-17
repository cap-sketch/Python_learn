#Dictionary
"""Dictionary is an unordered collection of key-value pairs.
   it is defined using curly braces {} and colons : to seperate key-value pairs.
   it is commonly used for data that needs to be looked up quickly."""

#empty dictionary
emp={}
print(type(emp),emp)

#dictionary with key value pairs
dict1={"name":"Anmol","age":21,"marks":7.5,"name":"hey"}
print(dict1)

#accessing value by key
print(dict1["name"])
print(dict1["age"])  #if key is not present it will give an error(KeyError)

#using get method to avoid keyerrors
print(dict1.get("age")) #returns None if key not found

#modifying and adding to dictionary
dict1["name"]="boy"     #modifying
dict1["class"]=4        #adding
print(dict1)

#length of dictionary
print(len(dict1))

#check if key is in dictionary(true or false)
print("name" in dict1)

#removing a key value pair(gives value of key in return)
removed=dict1.pop("class")
print(removed,dict1)