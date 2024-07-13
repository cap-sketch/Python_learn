###########Dictionary##############
#empty
dic={}
print(type(dic))

#accessing values
dic={"name":"Anmol","age":20,"class":"first"}
print(dic)
print(dic["name"]) #direct method
print(dic.get("name")) #using get method
dic.update({"home":"meerut"}) #addding or modifying
print(dic)

#deleting some data
del(dic["name"])
print(dic)
