flag=0
for i in range(3):
    password=input("enter password:")
    if password=="333":
        print("login successful")
        flag=1
        break
    else:
        print("incorrect password")
if not flag:
    print("account locaked")

