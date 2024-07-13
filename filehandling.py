f=open("new.txt","r")

#reading from a file
content=f.read(5)
print(content)

#read one line at a time
content=f.readline()
print(content)

content=f.readlines()
print(content)

#always close the file
f.close()

f=open("new.txt","w")
f.write("it's been a long day")

