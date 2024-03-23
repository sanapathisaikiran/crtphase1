n=12
sum=0
for i in range(1,12):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("greater",sum)
else:
    print("smaller",sum)