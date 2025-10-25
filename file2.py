cost=float(input("please enter the prise___"))
sp=float(input("please enter the sale amount___"))
if sp>cost:
    amount=sp-cost
    print("total profit is {0}".format(amount))
else:
    print("NO PROHIT!!!!")