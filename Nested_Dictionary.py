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

