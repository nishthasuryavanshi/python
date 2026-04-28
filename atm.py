balance=float(input("enter balance:"))
withdrow=float(input("enter withdraw amount:"))
if withdrow>(balance-1000):
    print("transaction failed :minimum balance should be 1000")
    
