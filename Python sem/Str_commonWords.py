#WAP to accept two strings and then display the common words
str1=input("enter the string: ")
str2=input("enter another string: ")

l1=str1.split()
l2=str2.split()
print(l1)
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
str3=" ".join(l3)
print(str3)        