amount=int(input("enter the amount:"))
premium=input("prmium membership(yes/no):")
if amount>=5000:
    amount=amount*0.8
elif amount>=2000:
    amount=amount*0.9

if premium=="yes":
    amount=amount*0.95
print("total bill:",amount)
