#WAP to convert time from 12 hour fomat to 24 hour format
"""time=12:15:60AM
        0123456789
            ..-2-1"""
def time_conversion(time):
    if time[-2:]=="AM" and time[:2]=="12":
        return "00"+time[2:-2]
    elif time[-2:]=="AM":
        return time[:-2]
    elif time[-2:]=="PM" and time[:2]=="12":
        return time[:-2]
    else:
        return str(int(time[:2])+12)+time[2:8]
    
time=input()
print(time_conversion(time))