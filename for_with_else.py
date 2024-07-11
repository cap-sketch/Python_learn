list=[1,2,3,4,5]
for i in list:
    if(i==3):
        print(" found")
        break
    print(i)
else:    #useful in cases of using break
    print("loop ended")     #if loop exit in between else will not work
                            #else will work if loop is executed completely.
