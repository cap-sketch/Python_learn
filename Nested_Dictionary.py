#nested dictionary
student={
    "name":"Anmol pratap",
    "subjects": {
        "phy": 45,
        "chem" :65,
        "maths":90,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["maths"])

#keys in dictionay
print(len(list(student.keys())))    #typecasting to list

#values in dictionary
print(student.values())

#return all key value pairs as tuple
print(student.items())
pairs=list(student.items())
print(pairs[0])

#return key according to value
print(student.get("name"))
print(student["name"])

