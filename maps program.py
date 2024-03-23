def P(n):
    if n%2==0:
        print(n**2)
    else:
        print(n**3)
j=[2,3,4,5]
b=map(P,j)
print(list(b))