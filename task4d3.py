n=12345
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
print(sum)