def fact(a):
    if(a==1 or a==0):
        return 1
    else:
        return a*fact(a-1)
    
print("the factorial is :",fact(5))    