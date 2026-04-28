password=input("enter the password")
#price100@
hasUpper=False
hasSymbol=False
hasDigit=False
hasLower=False
hasLen=len(password)>=0
for i in password:
    if i.isupper():
        hasUpper=True
    elif i.isdigit():
        hasDigit=True
    elif i.islower():
        hasLower=True
    else:
        hasSymbol=True
if hasSymbol and hasDigit and hasUpper and hasLen:
    print("strong")
else:
    print("weak")
