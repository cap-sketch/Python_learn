#string is plaindrome or not
def is_palindrome(a):
    a=a.replace(" ","").lower()
    return a==a[::-1]
str1=input()
if is_palindrome(str1):
    print("palindrome")
else:
    print("not a palindrome")