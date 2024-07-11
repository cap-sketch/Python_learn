######List######
list1=["hey",24.5,12,"boy",5,6.5]
print(list1)

#list indexing (can also be negative ...,-3,-2,-1)
print(list1[-1])

#list slicing[start :stop: step]
print(list1[0:4:2])

"""Adding Methods"""
#append method
list2=[]     #empty list
list2.append(11)
list2.append("hola")
print(list2)

#insert method---adding elements at any index
list2.insert(1,50)     #(index,value)
print(list2)

#extend method---adding multiple items at the same time at the end 
list2.extend([3,5,6.0,"amigo"])
print(list2)
list2.extend(list1)
print(list2)

"""Removing methods"""
#remove method
list1=[2,3,4,5,6]
a=list1.remove(2)  #returns None
# list1.remove(7) (gives value error) 
print(list1)

#pop function
""" -->removes last element by default
    -->for specific position,index can be passed as argument
    -->returns an element """

list1=[1,2,3,4,5]
a=list1.pop()     #pop last element by default
print(a)      
a=list1.pop(3)   #take index
print(a)
print(list)

#basic list operations
print(len(list1))    #length
print(list1+[6,7,8]) #concatenation
print(list1*4)       #repetition
print(3 in list1)    #membership
for x in list1:
    print(x)         #iteration
print()


#some inbuilt functions
list1=[1,2,3]
list2=[3,4,5]
str="hello"
print(max(list1)) #max of list
print(min(list1)) #min of list
print(list(str))  #type conversion
list3=list1.copy()  #copy the list
print(list3)
list1.clear()        #empty the list
print(list1)

l=list2.count(4)  #count occurence of element
print(l)

print(list2.index(5)) #index of element first occurence
list2.reverse()
print(list2)
list2.sort()
print(list2)




