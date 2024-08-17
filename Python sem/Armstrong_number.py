#armstrong number
"""also known as narcissistic number
   is a number that is equla to the sum of its own digits each raised to the power of the number of digits.
   example--  153=1^3+5^3+3^3"""

def armstrong(n):
    a=n
    sum=0
    while(a>0):
        r=a%10
        sum=sum+r*r*r
        a=a//10
    if sum==n:
        return True
    return False

n=int(input("enter any number: "))
if armstrong(n):
    print(n," is armstrong number")
else:
    print(n,"not an armstrong number")