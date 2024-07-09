#file handling
""" all files can be classified as ---text(.doc,.txt)
                                   ---binary(.mp4,.jpg)"""
f=open("demo.txt","r")
data=f.read(5)
print(data)
print(f.readline())
print(type(data))
f.close()

f=open("demo.txt","a")
f.write("hey boy")
f.close()

f=open("demo.txt","r")
print(f.read())
