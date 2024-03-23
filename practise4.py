ch=int(input("enter the classes:"))
ca=int(input("enter the attendance:"))
q=ca/ch*100
if q>75:
    print("student sit in exam",q)
else:
    print("cannot write the exam",q)