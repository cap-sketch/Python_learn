def leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else:
        return False
    
year=int(input("enter the year: "))
if leap(year):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")