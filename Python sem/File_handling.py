#File handling
"""python support file handling and allow users to handle files.
   ie. it allows you to read,write and perform many other operation on files.
   other languages support file handling but either lengthy or complex
   but in python it is easy and short.
   python treat files differently as binary or text files."""
#advantages
""" 1>versatality
    2>flexiblity
    3>user friendly
    4>cross platform"""
#disadvantages
""" 1>error prone
    2>security risk
    3>complexity
    4>performance"""

#open file f(pointer)=open("filename","file mode")l
f=open("hello.txt","w")
f.write("hello how u doing boy")
f.close()
f=open("hello.txt","rt")
content=f.read()
print(content)

f=open("hello2.txt","w+")
f.write("hello man")
f.seek(0)
content=f.read()
print(content)
f.close()