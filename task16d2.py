
for i in range(1,5):
    #spaces
    for j in range(1,5-i):
        print(" ",end=" ")
    #pattern
    for j in range(1,2*i):
        print("*",end=" ")
    print()