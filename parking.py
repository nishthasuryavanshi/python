no_of_hours =float(input("hours spend:"))
bill=0
if no_of_hours <= 2:
    bill=no_of_hours*100
elif no_of_hours<=5:
    bill=2*100+(no_of_hours-2)*50
else:
    bill=2*100+3*100+(no_of_hours-5)*25
print("total bill:",bill)
