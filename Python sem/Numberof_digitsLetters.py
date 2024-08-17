#WAP that accepts a sentence and calculate the number of digits, uppercase and lowercase letters.
str1=input("enter the sentence: ")
l=list(str1)
digits,uppers,lowers=0,0,0
for i in l:
    if i.isdigit():
        digits+=1
    if i.isupper():
        uppers+=1
    if i.islower():
        lowers+=1

print(digits,uppers,lowers)
