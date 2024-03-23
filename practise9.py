for i in range(1,6):
    #for spaces
    for j in range(1,6-i):
        print(" ",end=" ")
    #for pattern
    for j in range(1,2*i):
        print("*",end=" ")
    print()