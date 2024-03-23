n=47
n1=n
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
if n1%sum==0:
    print("divisible by",sum)
else:
    print("not divisible by",sum)