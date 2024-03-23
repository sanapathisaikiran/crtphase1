
for i in range(1,6):
    #spaces
    for j in range(1,6-i):
        print(" ",end=" ")
    #pattern
    for j in range(1,i+1):
        print("*",end=" ")
    print()