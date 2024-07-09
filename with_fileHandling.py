import os
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
    #close not needed (done automatically).
    os.remove("demo.txt")