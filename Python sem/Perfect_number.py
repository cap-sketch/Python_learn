def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    return False

n=int(input("enter any number: "))
if perfect_number(n):
    print(n," is perfect number")
else:
    print(n," is not a perfect number")