def isprime():
    c=1
    n=int(input("enter a numbe:"))
    for i in range(2,n):
        if n%i==0:
            c=0
            break
    if c==1:
        print("prime")
    else:
        print("not prime")
isprime()