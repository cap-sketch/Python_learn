def sumof(a):
    if(a==0):
        return 0
    else:
        return a+sumof(a-1)
    
print("the sum is ",sumof(5))    