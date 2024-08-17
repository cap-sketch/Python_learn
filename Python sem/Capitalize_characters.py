#WAP that accepts sequence of lines as input and print th elines after making all characters in the sentence capitalized.
def capitalize_lines():
    print("enter lines of text(type 'DONE' to finish): ")
    list1=[]
    while True:
        line=input()
        if line == "DONE":
            break
        else:
            list1.append(line.strip().upper())
    for lines in list1:
     print(lines)