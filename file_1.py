def count(file_path):
    vowels="aeiouAEIOU"
    constants="BCDFGHJKLMNPQRSTVWXYZ"
    constants=constants.lower()+constants

    n_vowels=0
    n_constants=0
    n_uppercase=0
    n_lowercase=0

    with open(file_path,"r") as file:
     content=file.read()
     for char in content:
        if char.isalpha():
            if char in vowels:
                n_vowels+=1
            if char in constants:
                n_constants+=1
            
            if char.isupper():
                n_uppercase+=1
            if char.islower():    
                n_lowercase+=1

    print("vowels:",n_vowels)
    print("constants:",n_constants)
    print("uppercase:",n_uppercase)
    print("lowercase:",n_lowercase)

filepath="new.txt"
count(filepath)                
