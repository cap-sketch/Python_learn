#WAP to check the validity of password input by users.

def valid(password):
    #for length
    if len(password)<6 or len(password)>12:
        return False
    
    symbol="$#@"
    has_upper=False
    has_lower=False
    has_symbol=False
    has_digit=False

    for char in password:
        if char.isupper():
            has_upper=True
        if char.islower():
            has_lower=True
        if char.isdigit():
            has_digit=True
        if char in symbol:
            has_symbol=True
    return has_upper and has_lower and has_digit and has_symbol

password=["anmol","Adf@2343","tada","agGg23@"]
lis=[]
for i in password:
    if valid(i):
        lis.append(i)
print(lis)