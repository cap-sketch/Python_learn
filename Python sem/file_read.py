#reading from the file
f=open("hello.txt","r")
#read the entire file
content=f.read()
print(content)

f.seek(0) #get the pointer back
#read one line only
content=f.readline()
print(content)

f.seek(0)
#read all lines into list
content=f.readlines()
print(content)

#tell pointer position
print(f.tell())
f.seek(0)
print(f.tell())

#reading a fixed number of characters
content=f.read(5)
print(content)
f.close()

#automatically closing method (use with keyword)
with open("hello.txt","r") as f:
    content=f.read()
    print(content)