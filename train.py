avail=0
seats=int(input("sets required:"))
vip=input("enter vipo status(ys/no):")
if vip=="yes" or seats<avail:
    print("tickect confiremed")
else:
    print("waiting...")