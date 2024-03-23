n=153
n1=n
n2=n1
count=0
sum=0
while n>0:
    n=n//10
    count=count+1
while n1>0:
    d=n1%10
    sum=d**count+sum
    n1=n1//10
if sum==n2:
    print("yes",sum)
else:
    print("no",sum)
