#List comprehension
"""List comprehension offers a shorter syntax for creating a list bases on the values of existing list.
   it is used to replace loop making code concise,clear and often faster.
   synata-[expression for item in iteration if condition]
         -use square braces
         -expression is output of current item in iteration
         -for item in iteration is loop
         -if condition is optional"""
#list containing even numbers from 0 to 9
list1=[x for x in range(10) if x%2==0]
print(list1)