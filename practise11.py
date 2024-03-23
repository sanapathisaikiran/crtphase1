for i in range(1,6):
    for j in range(1, i+1):
        print(i,end=" ")
    print()
n=1
for i in range(4,0,-1):
    for j in range(i):
        print(i,end=" ")
        n=n+1
    print()