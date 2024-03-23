n=int(input())
space1 = ""
for i in range(0,(n)):
    space1 = " "*(n-i) + "*"
    print(space1)
print(("*"+" ")*n)