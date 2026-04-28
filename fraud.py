amount=int(input("enter the amount:"))
location=input("enter the location (yes/no):")
transaction=0
if (amount > 50000 and location=="No") or (transaction> 3):
    print("Fraud Detected")
else:
    print("Transaction Safe")