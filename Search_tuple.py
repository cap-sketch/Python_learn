tuple=(1,4,9,16,25,36,49,64,81,100)
n=int(input("number to search: "))
l=len(tuple)
while(l>0):
    if(n==tuple[l-1]):
        print("the number is found")
        break
    else:
        if(l==1):
           print("not found")    
    l-=1