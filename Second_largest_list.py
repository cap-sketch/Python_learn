#find second largest element in a list
list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n+1):
    element=int(input("enter the element: "))
    list1.append(element)
list1.sort()    
print("second largest",list1[n-1])    
