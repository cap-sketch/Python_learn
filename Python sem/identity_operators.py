#Identity operators
"""identity operators are used to check wheather objects 
   are of same data type or they share same memory location.
   is , is not
   output- true,false"""
a=5
b=5

"""note unlike c,c++ . here a and b are given same memory
   location with pointers a,b."""
print(id(a))
print(id(b))
"""identity operators check if memory location is same or not."""
print(a is b)
print(a is not b)
print(type(a) is int)
print(type(a) is type(b))
"""note- ==.. checks values
         is.. checks memory location"""