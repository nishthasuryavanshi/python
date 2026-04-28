no_of_unit = int(input("units consumed:"))
bill = 50
if no_of_unit <= 100:
    bill += no_of_unit * 1.5
elif no_of_unit <= 200:
    bill += 100 * 1.5 + (no_of_unit - 100) * 3.5
else:
    bill += 100 * 1.5 + 100 * 3.5 + (no_of_unit - 200) * 5
if bill>2000:
    bill=bill*1.1
print("total bill:", bill)