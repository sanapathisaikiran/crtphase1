n=12
sum=0
r=1
for r in range(1,12):
    if n%r==0:
       sum=sum+r
if sum>n:
    print("greater",sum)
else:
    print("smaller",sum)
