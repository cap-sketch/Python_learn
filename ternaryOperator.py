#ternary operator/ single line if
#  <var>=<val1> if <condition> else <val2>
food=input("food: ")
eat="yes" if (food=="cake") else "no"
print(eat)

#clever if
#  <var>=(false_val,true_val) [<condition>]
age=int(input("age: "))
vote=("yes","no") [age<18]
print(vote)