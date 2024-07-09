#Dictionary---are used to store data values in key:value pairs.
#             they are unordered-any value can come at any place
#             ,mutable & don't allow duplicate keys.

info={
    "key":"value",
    "name":"anmol",
    "learning":"python",
    "age":35,
    "isAdult":True,
    "marks":94.4,
    "subjects":["python","java","C"],
    "topics":("dictionary","set"),
    95:"myrollnumber",
}
#in value almost all the data types are acceptable.

#keys can be int, float , string ,bollean, tuple(immutable).
#whereas in keys list are not allowed.
print(info)
print(info["name"])
print(info[95])

#modify
info["name"]="sheer"
print(info["name"])

#add new
info["surname"]="Pratap"
print(info["surname"])