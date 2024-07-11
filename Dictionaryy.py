########Dictionary#########
"""-->Dictionary is an unordered collection of key-value pairs.
   -->it is defined using curly braces{} and colons : to 
   seperate key and values.
   -->Dictionary is mapping technique used for data that 
   needs to be looked up quickly."""

"""creating dictionary"""
#empty dictionary
dict1={}
print(dict1,type(dict1))

#dictionary with key:value pairs
dict1={"Name":"Anmol","age":20,"marks":8.1}
print(dict1)


"""accessing elements"""
#values by key
print(dict1["Name"])
print(dict1["age"])
print(dict1["marks"])

#using get method to avoid key errors
dict1={"Name":"Anmol","age":20,"school":None,"marks":8.1}
print(dict1.get("Name"))


"""modifying and Adding"""
#modifying a value
dict1["Name"]="cheetah"
print(dict1)

#adding a new key value pair
dict1["city"]="Meerut"
print(dict1)


"""Operations"""
#length
print(len(dict1))

#checking if key is in dictionary
print("Name" in dict1)

#removing a key:value pair
removed=dict1.pop("age")
print(removed)
print(dict1)