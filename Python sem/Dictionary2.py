#dictionary
"""dictionary is a collection of key values used to store data values like a map
   key:value pair sepearted by colon
   keys are uniques and immutable such as string,numbers,or tuples."""


#empty dictionary
dict1={}
print(type(dict1))

dict2={
    "name":"anmol","class":4,"age":22
}
#access value
print(dict2["name"])

#using get() method
print(dict2.get("class"))

#update dictionary
dict2.update({"year":2})
print(dict2)

#deleting elements
del dict2["name"]
print(dict2)