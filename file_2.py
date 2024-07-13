f=open("new.txt","r")
f2=open("new2.txt","w")

digits="0123456789"
n_alpha=0
n_digits=0

for char in f:
    if char.isalpha():
        n_alpha+=1
    if char in digits:
        n_digits+=1
    
f2.write(f"letters are {n_alpha}\ndigits are {n_digits}")
f.close()
f2.close()