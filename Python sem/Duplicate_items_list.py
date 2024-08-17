#Removing duplicate items from the list
list1=[]
n=int(input("enter the no of elements in list: "))
print("enter the elements: ")
for i in range(0,n):
    b=int(input())
    list1.append(b)
print(list1)

list2=[]
for item in list1:
  if item not in list2:
    list2.append(item)
print(list2)

#another method(using a set)
list3=list(set(list1))
print(list3)