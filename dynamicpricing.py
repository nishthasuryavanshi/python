base=int(input("enter the base:"))
demand=int(input("enter the demand(high/low):"))
weekend=input("enter the day (yes/no):")
if demand =="high" and weekend =="yes":
    base=base*1.3
elif demand =="high":
    base=base*1.2
elif weekend =="yes":
    base=base*1.1
print("final price:",base)
