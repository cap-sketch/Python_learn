#while loop
"""the while loop executes a block of code as long as a specified condition remains true."""
#basic while loop
count=1
while(count<=5):
    print(count)
    count+=1

# #while loop with user input
# user=int(input("enter the pin:"))
# pin=123
# while user!=pin:
#     print("incorrect pin")
#     print("try again...")
#     user=int(input("enter the pin: "))
# print("Access granted")

# #infinite loop
# while True:
#     user=input("enter the number(type exit to return): ")
#     if user =="exit":
#         break
#     else:
#         print(f"you entered {user} number")

#using else with while loop
count=0
print()
while count<5:
    print(count)
    count+=1
else:
    print("loop finished")

#continue
"""the continue statement is used to skip the remaining code inside the loop for the current iteration and move to the next iteration."""
count=0
while count<=5:
    count+=1    
    if count==3:
        continue
    else:
        print(count)
  
#while loop with else and break
count=0
while count<=5:
   if count==4:
       break
   else:
       print(count)
   count+=1
else:
    print("loop finished")           #note-the else statement will not be executed if the loop is terminated by break statement.

    