with open("input.txt","w+") as file1,open ("odd.txt","w") as file2,open("even.text","w") as file3:
    file1.write("23467765")
    file1.seek(0)
    content=file1.read()
    for char in content:
        if int(char)%2==0:
            file3.write(str(char))
        if int(char)%2!=0:
            file2.write(str(char))
