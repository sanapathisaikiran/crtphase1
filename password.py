def login():
    username=input("username:")
    password=input("password:")
    c=1
    if username==password:
        c=0
    if c==0:
        print("login successful")
    else:
        print("invalid,try again")
login()