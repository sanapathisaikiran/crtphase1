def l():
    n=1
    while n!=0:
      a=int(input("username"))
      b=int(input("password"))
      if a==b:
        print("login succeful")
        n=0
      else:
        print("invalid enter again")
l()