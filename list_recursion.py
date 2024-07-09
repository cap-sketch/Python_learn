def printer(list,index=0):
    l=len(list)
    if(index==l):
       return

    print(list[index])
    printer(list,index+1)      
    
list=[2,3,4,5,6,6,2,3]    
printer(list)    