#Membership operators
"""used to check if value is a member of a sequence(list,tuple,etc.)"""
reg_user=["anmol","rahul","shyam"]
name=input("enter your name: ")
if name in reg_user:
    print("welcome ",name)
else:
    print("you are not authorised")
