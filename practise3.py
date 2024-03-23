quantity=int(input("enter the quantity:"))
if quantity>1000:
    print("the total priceis",quantity-0.01*quantity)
else:
    print("no discount the price is",quantity)