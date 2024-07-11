#########while loops#########
"""basic """
count=0
while(count<5):
    print(f"count:{count}")
    count+=1

"""infinite loop"""
while True:
    user=input("enter a number('exit' to stop):")
    if user=="exit":
        break
    else:
        print(f"you entered: {user}")

"""using else with while""" 
num=0
while num<5:
    print(f"Num:{num}")
    num+=1
else:
    print("loop finished")   


""""while looop using continue """  
num=0
while num<5:
    num+=1
    if num==3:
        continue
    print(f"Num: {num} ")  


"""while loop with else and break"""
num=0
while num<5:
    print(f"Num:{num}")
    num+=1
    if num==3:
        break
    else:
        print("loop finished")    

