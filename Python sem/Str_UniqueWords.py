#WAP to display unique words from the string
str1=input("enter the string: ")
l=str1.split()
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
str1=" ".join(l1)
print(str1)