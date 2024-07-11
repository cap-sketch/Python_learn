#range()
"""Range function returns a sequence of number,
    starting from 0 by default, and increments by
    1 by default, and stops before a specified number.
        range(Start?,Stop,Step?)   
        *can be written as: 
                           --range(stop)
                           --range(start,stop)
                           --range(start,stop,step) """
#printing the range function directly
print(range(5))
print()

#using a variable for range function
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print()

#using variable as range in loop
for i in seq:
    print(i)


print("\n using loop")
#one way
for i in range(5):
    print(i)
#second way
for i in range(2,7):
    print(i)
#third way
for i in range(2,10,2):
    print(i)