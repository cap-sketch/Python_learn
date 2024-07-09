#range()
"""Range function returns a sequence of number,
    starting from 0 by default, and increments by
    1 by default, and stops before a specified number.
        range(Start?,Stop,Step?)   """

print(range(5))
print()
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print()

for i in seq:
    print(i)


print("\nusing loop")
for i in range(2,7,2):
    print(i)