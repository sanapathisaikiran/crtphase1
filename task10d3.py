n=153
n1=n
n2=n1
sum=0
count=0
while n>0:
    n=n//10
    count=count+1
while n1>0:
    d=n1%10
    n1=n1//10
    sum=d**count+sum
print(sum)
    

