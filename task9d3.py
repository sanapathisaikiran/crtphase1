n=47
sum=0
n1=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
if n1%sum==0:
    print("divisible")
else:
    print("not divisible")
