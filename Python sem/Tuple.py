#Tuple
"""tuple is a sequence of immutable objects.
   repersented using parenthesis and commas.
   just like list except elements are immutable."""



#empty tuple
tup=()
print(tup)

#creating tuple with single value
tup=1,
print(type(tup))
print(tup)
# tup2=(2)     act as integer
tup2=(2,)
print(type(tup2))

#accessing values and slicing
tup1=("physics","chemistry",1997,2000)
tup2=(1,2,3,4,5,6,7)
print(tup1[0])
print(tup1[1])
print(tup2[0:5:2])

"""NOTE--we can change any collection(list ,tuple ,set) from one data type to another 
       --but cannot chage int,float into python collection.(int cannot be change into list and viceversa)"""

#tuple deletion
tup3=tup2
print(tup3)
del tup3
# print(tup3)   Name error


"""Basic tuple operation"""
tup2=(1,2,3,4,5,6,7)

#length
print(len(tup2))

#concatenation
print(tup2+tup1)

#repetetion
print(tup2*2)

#membership
print(5 in tup2)

#iteration
for i in tup2:
    print(i)
print()

"""max and min value"""
print(max(tup2))
print(min(tup2))