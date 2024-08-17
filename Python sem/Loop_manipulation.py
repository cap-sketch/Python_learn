#Loop manipulation
"""loop manipulation statements like pass,continue,break, and else provide ways to control the flow of loops."""

#Pass
"""the pass statement is a no operation statement that serves as a placeholder when syntactically some code is required,
   but you don't want to execute any specific operation."""

for count in range(0,6):
    if count==2:
        pass     #do nothing
    else:
        print(count)

#continue
"""the continue statement is used in the loop manipulation as it skips the code for current iteration and move to the next iteration."""
for count in range(0,6):
    if count==2:
        continue
    else:
        print(count)

#break
"""the break statement is used to exit the loop prematurely.
   it terminates the loop when a certain condition is met."""
for i in range(0,5):
    if i==4:
        break
    else:
        print(i)

#else
"""the else clause in a loop is executed when the loop conditions becomes false.
   however when the loop statement is terminated by break statement,the else clause is skipped."""
