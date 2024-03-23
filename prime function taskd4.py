def prime():
    c=1
    count=0
    num=int(input("enter a number:"))
    for i in range(2,num):
        if num%c==0:
            c=c+1
            count=count+c
    if count<=2:
        print("prime")
    else:
        print("not prime")
prime()