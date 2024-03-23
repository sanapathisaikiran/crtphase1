for i in range(1,6):
    #for spaces
    for j in range(1,5-i+1):
        print(" ",end=" ")
    #for pattern
    for i in range(1,i+1):
        print("*",end=" ")
    print()