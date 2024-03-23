math=int(input("enter the math:"))
science=int(input("enter the science:"))
social=int(input("enetr the social:"))
if math>80 and science>80 and social>80:
    print("A+")
elif 60<math<80 and 60<science<80 and 60<social<80:
    print("B+")
else:
    print("pass")