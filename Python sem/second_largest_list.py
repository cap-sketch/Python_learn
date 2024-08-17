#finding the second largest number in the list
list1=[]
print("enter the number of elements in a list: ")
n=int(input())
print("enter the elements : ")
for i in range(0,n):
    a=int(input())
    list1.append(a)
list1.sort()
print("the second max element is : ",list1[n-2])
