#Membership operators
"""These operators used to test wheather a specific value
or item is present withing  a sequence,such as string,list,tuple or set."""
# 'in' and 'not in' are membership operators
# return true or false as output

list1=[1,2,3,4,5]
print(5 in list1)
print(5 not in list1)

reg_user=["varun","anmol","ravi","nitin"]
name=input("enter your name: ")
if name in reg_user:
    print("access granted")
else:
    print("access denied")

str="hello"
str[1]="a"