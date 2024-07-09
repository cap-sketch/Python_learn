#lists--a built in data type that stores set of values
#     --it can store elements of different types(int,float,string,etc)
#     --list are mutable.
marks=[34,54,64,23,63,62,"hello",84.5]
print(marks)
print(type(marks))
print(type(marks[7]))

marks[0]="hey"    #list are mutable(changeable)
print(marks[0])
print(marks[1])

print(len(marks))

#list slicing
print(marks[1:3])

marks.append(5)
print(marks)

#sorting the list
list=[3,5,4]
list.sort()
print(list)
#sorting in reverse order
list.sort(reverse=True)
print(list)
#reversing the list
list.reverse()
print(list)

#we can also sort the strings
list1=["banana","litchi","apple"]
list1.sort()
print(list1)

#inserting elements at particular index
list.insert(1,56)
print(list)

#remove()--remove the first occurence of element
list.remove(4)
print(list)

#removes element at index
list.pop(2)
print(list)
list