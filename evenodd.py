num=int(input("enter a number:"))
even,odd=0,0
while(num):
    if num%2==0:
        even+=1
    else:
        odd+=1
    num=int(input("enter a number:"))
print("even:",even)
print("odd:",odd)