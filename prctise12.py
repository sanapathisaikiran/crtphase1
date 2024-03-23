for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
n=3
for i in range(6,12):
    for j in range(1,11-i):
        print(i,end=" ")
    n=n-1
    print()