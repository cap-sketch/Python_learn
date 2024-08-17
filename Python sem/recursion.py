#recursion
"""process of function calling itself
   should have a base condition"""

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)

print(fact(5))