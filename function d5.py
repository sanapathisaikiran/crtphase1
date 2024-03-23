def check(n):
      d=n%10
      if d==5:
        return n**2
      if d==3:
        return n**3
      if d==6:
        return n-1
      else:
        return n/2
a=check(5)
print(a)