#remove duplicate elements
a=[]
n=int(input("enter the number of elements in list:"))
for i in range(0,n):
    element=int(input("enter the element: "))
    a.append(element)
b=[]
[b.append(i) for i in a if i not in b]
print(b)
