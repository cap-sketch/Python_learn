#lists
"""list is a sequence data type which is used to store collection of data.
   list are mutable in nature.
   list are not homogenous,can store different data types like int,float,string.
   list are repersented using square braces and seperated by commas.
   """
#empty list
list1=[]
print(list1,type(list1))

#list with different data type
list1=["hello","boy",1,2,3.4,"hey"]
print(list1)
print(len(list1))

#list indexing 
print(list1[0])
list1[0]=5   #modifying as list are mutable
print(list1)

#list slicing
"""it can be repersented as list[start,stop,step]"""
print(list1[0:4:2])



"""adding elements to list"""
#using append -adding only one element at a time at the end of list
list1=[]
list1.append("hello")
list1.append("hola")
list1.append(5)
print(list1)

#using insert--adding only one element at a time but at the desired position ->> insert(index,value)
list1.insert(0,"rata")
list1.insert(3,56)
print(list1)

#using extend--add multiple items at one time at the end of list
list1.extend(["tada",5.4])
print(list1)



"""removing elements from the list"""
#using inbuilt remove() function--but error arises if the element does not exist in the list
list1=["hello","boy",1,2,3.4,"hey"]
list1.remove("hello")
print(list1)
# list1.remove("hell")   valueError-element not in the list

#pop() function removes the last value of list by default
#but we can also pass index of element as argument
list1.pop()
print(list1)
list1.pop(0)
print(list1)
# list1.pop(3.4)        TypeError-float is not a index
